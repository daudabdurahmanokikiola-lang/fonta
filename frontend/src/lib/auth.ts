// ===========================================
// FONTA AI STUDY COMPANION - AUTHENTICATION
// ===========================================

/**
 * Simple authentication service for Fonta AI Study Companion.
 * Replaces Supabase authentication with local state management.
 * 
 * Note: This is a basic implementation. For production, consider
 * implementing proper JWT authentication with the backend.
 */

export interface User {
  id: string;
  email: string;
  name: string;
  created_at: string;
  updated_at: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}

class AuthService {
  private user: User | null = null;
  private listeners: ((state: AuthState) => void)[] = [];

  constructor() {
    // Check for stored user data
    this.loadUserFromStorage();
  }

  private loadUserFromStorage(): void {
    try {
      const storedUser = localStorage.getItem('fonta_user');
      if (storedUser) {
        this.user = JSON.parse(storedUser);
        this.notifyListeners();
      }
    } catch (error) {
      console.error('Error loading user from storage:', error);
      this.user = null;
    }
  }

  private saveUserToStorage(user: User | null): void {
    try {
      if (user) {
        localStorage.setItem('fonta_user', JSON.stringify(user));
      } else {
        localStorage.removeItem('fonta_user');
      }
    } catch (error) {
      console.error('Error saving user to storage:', error);
    }
  }

  private notifyListeners(): void {
    const state: AuthState = {
      user: this.user,
      isAuthenticated: !!this.user,
      isLoading: false,
    };
    this.listeners.forEach(listener => listener(state));
  }

  // Subscribe to auth state changes
  subscribe(listener: (state: AuthState) => void): () => void {
    this.listeners.push(listener);
    
    // Return unsubscribe function
    return () => {
      const index = this.listeners.indexOf(listener);
      if (index > -1) {
        this.listeners.splice(index, 1);
      }
    };
  }

  // Get current auth state
  getCurrentState(): AuthState {
    return {
      user: this.user,
      isAuthenticated: !!this.user,
      isLoading: false,
    };
  }

  // Sign up (placeholder - implement with backend)
  async signUp(email: string, password: string, name: string): Promise<{ user: User | null; error: string | null }> {
    try {
      // TODO: Implement actual signup with backend API
      // For now, create a mock user
      const user: User = {
        id: Date.now().toString(),
        email,
        name,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };

      this.user = user;
      this.saveUserToStorage(user);
      this.notifyListeners();

      return { user, error: null };
    } catch (error) {
      return { 
        user: null, 
        error: error instanceof Error ? error.message : 'Signup failed' 
      };
    }
  }

  // Sign in (placeholder - implement with backend)
  async signIn(email: string, password: string): Promise<{ user: User | null; error: string | null }> {
    try {
      // TODO: Implement actual signin with backend API
      // For now, create a mock user
      const user: User = {
        id: Date.now().toString(),
        email,
        name: email.split('@')[0],
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };

      this.user = user;
      this.saveUserToStorage(user);
      this.notifyListeners();

      return { user, error: null };
    } catch (error) {
      return { 
        user: null, 
        error: error instanceof Error ? error.message : 'Signin failed' 
      };
    }
  }

  // Sign out
  async signOut(): Promise<{ error: string | null }> {
    try {
      this.user = null;
      this.saveUserToStorage(null);
      this.notifyListeners();
      return { error: null };
    } catch (error) {
      return { 
        error: error instanceof Error ? error.message : 'Signout failed' 
      };
    }
  }

  // Get current user
  getCurrentUser(): User | null {
    return this.user;
  }

  // Check if user is authenticated
  isAuthenticated(): boolean {
    return !!this.user;
  }
}

// Export singleton instance
export const authService = new AuthService();
export default authService;
