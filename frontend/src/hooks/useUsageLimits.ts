import { useState, useEffect } from 'react';
import { apiService } from '../lib/api';

export function useUsageLimits(userId: string) {
  const [totalUsage, setTotalUsage] = useState(0);
  const [canUse, setCanUse] = useState(true);
  const [timeUntilReset, setTimeUntilReset] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (userId) {
      loadUsageData();
      // Set up interval to update time until reset
      const interval = setInterval(() => {
        updateTimeUntilReset();
      }, 60000); // Update every minute

      return () => clearInterval(interval);
    }
  }, [userId]);

  const loadUsageData = async () => {
    try {
      // TODO: Implement usage limits API endpoint
      // For now, use mock data
      setTotalUsage(0);
      setCanUse(true);
      setTimeUntilReset(6 * 60 * 60 * 1000); // 6 hours
    } catch (error) {
      console.error('Error loading usage data:', error);
    } finally {
      setLoading(false);
    }
  };

  const calculateTimeUntilReset = (lastReset: string) => {
    const resetTime = new Date(lastReset).getTime() + 6 * 60 * 60 * 1000;
    return Math.max(0, resetTime - new Date().getTime());
  };

  const updateTimeUntilReset = () => {
    if (totalUsage >= 15) {
      loadUsageData(); // Reload to check if reset time has passed
    }
  };

  const incrementUsage = async () => {
    if (!canUse) return false;

    try {
      const today = new Date().toISOString().split('T')[0];
      
      // TODO: Implement usage increment API endpoint
      // const response = await apiService.incrementUsage(userId);
      
      // For now, just increment locally
      const newTotal = totalUsage + 1;
      setTotalUsage(newTotal);
      setCanUse(newTotal < 15);
      return true;
    } catch (error) {
      console.error('Error incrementing usage:', error);
    }
    return false;
  };

  const resetUsage = async () => {
    try {
      const today = new Date().toISOString().split('T')[0];
      
      // TODO: Implement usage reset API endpoint
      // const response = await apiService.resetUsage(userId);
      
      // For now, just reset locally
      setTotalUsage(0);
      setCanUse(true);
      setTimeUntilReset(6 * 60 * 60 * 1000);
    } catch (error) {
      console.error('Error resetting usage:', error);
    }
  };

  return {
    totalUsage,
    canUse,
    timeUntilReset,
    loading,
    incrementUsage,
    resetUsage,
    remainingUses: Math.max(0, 15 - totalUsage)
  };
}