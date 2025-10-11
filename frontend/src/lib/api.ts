// ===========================================
// FONTA AI STUDY COMPANION - API SERVICE
// ===========================================

/**
 * API service for communicating with the Fonta AI backend.
 * Replaces Supabase integration with direct API calls.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

export interface ApiResponse<T = any> {
  status: 'success' | 'error';
  data?: T;
  message?: string;
  error?: string;
}

export interface User {
  id: string;
  email: string;
  name: string;
  created_at: string;
  updated_at: string;
}

export interface Quiz {
  id: string;
  user_id: string;
  title: string;
  questions: any[];
  created_at: string;
  updated_at: string;
}

export interface Summary {
  id: string;
  user_id: string;
  title: string;
  content: string;
  original_text: string;
  created_at: string;
  updated_at: string;
}

export interface HomeworkHelp {
  id: string;
  user_id: string;
  question: string;
  answer: string;
  subject: string;
  created_at: string;
  updated_at: string;
}

class ApiService {
  private baseUrl: string;

  constructor() {
    this.baseUrl = API_BASE_URL;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
        ...options,
      });

      const data = await response.json();

      if (!response.ok) {
        return {
          status: 'error',
          error: data.message || 'An error occurred',
        };
      }

      return {
        status: 'success',
        data,
      };
    } catch (error) {
      return {
        status: 'error',
        error: error instanceof Error ? error.message : 'Network error',
      };
    }
  }

  // Health check
  async healthCheck(): Promise<ApiResponse> {
    return this.request('/api/health');
  }

  // Test endpoint
  async testConnection(): Promise<ApiResponse> {
    return this.request('/api/test');
  }

  // User management (placeholder - implement based on your auth system)
  async createUser(userData: Partial<User>): Promise<ApiResponse<User>> {
    return this.request('/api/users', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  }

  async getUser(userId: string): Promise<ApiResponse<User>> {
    return this.request(`/api/users/${userId}`);
  }

  // Quiz management
  async createQuiz(quizData: Partial<Quiz>): Promise<ApiResponse<Quiz>> {
    return this.request('/api/quizzes', {
      method: 'POST',
      body: JSON.stringify(quizData),
    });
  }

  async getQuizzes(userId: string): Promise<ApiResponse<Quiz[]>> {
    return this.request(`/api/quizzes?user_id=${userId}`);
  }

  async getQuiz(quizId: string): Promise<ApiResponse<Quiz>> {
    return this.request(`/api/quizzes/${quizId}`);
  }

  // Summary management
  async createSummary(summaryData: Partial<Summary>): Promise<ApiResponse<Summary>> {
    return this.request('/api/summaries', {
      method: 'POST',
      body: JSON.stringify(summaryData),
    });
  }

  async getSummaries(userId: string): Promise<ApiResponse<Summary[]>> {
    return this.request(`/api/summaries?user_id=${userId}`);
  }

  async getSummary(summaryId: string): Promise<ApiResponse<Summary>> {
    return this.request(`/api/summaries/${summaryId}`);
  }

  // Homework help management
  async createHomeworkHelp(homeworkData: Partial<HomeworkHelp>): Promise<ApiResponse<HomeworkHelp>> {
    return this.request('/api/homework', {
      method: 'POST',
      body: JSON.stringify(homeworkData),
    });
  }

  async getHomeworkHelp(userId: string): Promise<ApiResponse<HomeworkHelp[]>> {
    return this.request(`/api/homework?user_id=${userId}`);
  }

  // AI processing endpoints
  async generateQuiz(text: string, options?: any): Promise<ApiResponse> {
    return this.request('/api/ai/generate-quiz', {
      method: 'POST',
      body: JSON.stringify({ text, options }),
    });
  }

  async generateSummary(text: string, options?: any): Promise<ApiResponse> {
    return this.request('/api/ai/generate-summary', {
      method: 'POST',
      body: JSON.stringify({ text, options }),
    });
  }

  async getHomeworkHelp(text: string, subject: string): Promise<ApiResponse> {
    return this.request('/api/ai/homework-help', {
      method: 'POST',
      body: JSON.stringify({ text, subject }),
    });
  }
}

// Export singleton instance
export const apiService = new ApiService();
export default apiService;
