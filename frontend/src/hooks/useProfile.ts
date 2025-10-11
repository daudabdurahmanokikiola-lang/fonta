import { useState, useEffect } from 'react';
import { User } from '../lib/auth';
import { apiService } from '../lib/api';

export interface Profile {
  id: string;
  user_id: string;
  email: string;
  full_name: string;
  subscription_type: 'free' | 'premium';
  quiz_count: number;
  summary_count: number;
  homework_count: number;
  current_streak: number;
  longest_streak: number;
  last_activity: string;
  created_at: string;
  updated_at: string;
}

export function useProfile(user: User | null) {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) {
      setProfile(null);
      setLoading(false);
      return;
    }

    fetchProfile();
  }, [user]);

  const fetchProfile = async () => {
    if (!user) return;

    const response = await apiService.getUser(user.id);
    if (response.status === 'success' && response.data) {
      setProfile(response.data as Profile);
    }
    setLoading(false);
  };

  const updateProfile = async (updates: Partial<Profile>) => {
    if (!user) return;

    // TODO: Implement profile update API endpoint
    const response = await apiService.getUser(user.id);
    if (response.status === 'success' && response.data) {
      setProfile(response.data as Profile);
    }

    return { data: response.data, error: response.error };
  };

  const incrementUsage = async (type: 'quiz' | 'summary' | 'homework') => {
    if (!profile) return;

    const field = `${type}_count`;
    const newCount = (profile[field as keyof Profile] as number) + 1;
    
    // Update streak logic
    const today = new Date().toDateString();
    const lastActivity = profile.last_activity ? new Date(profile.last_activity).toDateString() : null;
    
    let newStreak = profile.current_streak;
    if (lastActivity !== today) {
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      
      if (lastActivity === yesterday.toDateString()) {
        newStreak += 1;
      } else {
        newStreak = 1;
      }
    }

    const updates = {
      [field]: newCount,
      current_streak: newStreak,
      longest_streak: Math.max(profile.longest_streak, newStreak),
      last_activity: new Date().toISOString(),
    };

    await updateProfile(updates);
  };

  const canUseFeature = (type: 'quiz' | 'summary' | 'homework') => {
    if (!profile) return false;
    if (profile.subscription_type === 'premium') return true;

    const limits = { quiz: 3, summary: 2, homework: 1 };
    const field = `${type}_count`;
    const currentCount = profile[field as keyof Profile] as number;
    
    return currentCount < limits[type];
  };

  return { profile, loading, updateProfile, incrementUsage, canUseFeature, fetchProfile };
}