import { useState, useEffect } from 'react';
import { authService, User, AuthState } from '../lib/auth';

export function useAuth() {
  const [authState, setAuthState] = useState<AuthState>({
    user: null,
    isAuthenticated: false,
    isLoading: true,
  });

  useEffect(() => {
    // Get initial state
    setAuthState(authService.getCurrentState());

    // Subscribe to auth state changes
    const unsubscribe = authService.subscribe((state) => {
      setAuthState(state);
    });

    return unsubscribe;
  }, []);

  const signUp = async (email: string, password: string, fullName: string) => {
    const { user, error } = await authService.signUp(email, password, fullName);
    return { data: { user }, error };
  };

  const signIn = async (email: string, password: string) => {
    const { user, error } = await authService.signIn(email, password);
    return { data: { user }, error };
  };

  const signOut = async () => {
    const { error } = await authService.signOut();
    return { error };
  };

  return { 
    user: authState.user, 
    loading: authState.isLoading, 
    signUp, 
    signIn, 
    signOut 
  };
}