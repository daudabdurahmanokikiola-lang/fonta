# 🤝 Contributing to Fonta AI Study Companion

Thank you for your interest in contributing to Fonta AI Study Companion! This guide will help you get started with contributing to our project.

## 🚀 Quick Start

### 1. Fork and Clone
```bash
git clone https://github.com/your-username/fonta-ai-study-companion.git
cd fonta-ai-study-companion
```

### 2. Setup Development Environment

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
uvicorn app:app --reload
```

### 3. Create Environment Files
```bash
# Copy environment templates
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit the .env files with your configuration
```

## 📁 Project Structure

```
fonta-ai-study-companion/
├── frontend/           # React + Vite + TypeScript
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/            # Python FastAPI
│   ├── app.py
│   ├── models/
│   │   └── ai/        # AI logic modules
│   ├── routes/
│   └── utils/
├── .gitignore
├── README.md
└── CONTRIBUTING.md
```

## 🔄 Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Changes
- Write clean, readable code
- Add comments for complex logic
- Follow existing code style
- Test your changes locally

### 3. Commit Changes
```bash
git add .
git commit -m "feat(scope): description of changes"
```

**Commit Message Format:**
- `feat(scope):` - New features
- `fix(scope):` - Bug fixes
- `docs(scope):` - Documentation updates
- `style(scope):` - Code style changes
- `refactor(scope):` - Code refactoring
- `test(scope):` - Test additions/changes

### 4. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 🎯 Areas for Contribution

### Frontend (React + TypeScript)
- UI components and layouts
- User experience improvements
- API integration
- File upload functionality
- Quiz and summary displays

### Backend (Python + FastAPI)
- API endpoints and routes
- Database integration (MongoDB)
- AI logic implementation
- File processing
- Authentication and security

### AI Logic (Python)
- Quiz generation algorithms
- Text summarization
- Natural language processing
- Model training and optimization

## 📋 Code Standards

### Frontend
- Use TypeScript for type safety
- Follow React best practices
- Use Tailwind CSS for styling
- Write responsive components
- Add PropTypes or TypeScript interfaces

### Backend
- Follow PEP 8 Python style guide
- Use type hints
- Write docstrings for functions
- Handle errors gracefully
- Use async/await for async operations

### General
- Write meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Test your code before submitting
- Update documentation when needed

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm run test
npm run lint
```

### Backend Testing
```bash
cd backend
python -m pytest
python -m flake8
```

## 📝 Documentation

- Update README.md for major changes
- Add JSDoc comments for functions
- Update API documentation
- Include examples in docstrings

## 🐛 Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details (OS, Node version, Python version)

## 💡 Suggesting Features

For feature suggestions:
- Check existing issues first
- Provide clear use case
- Explain the benefit to users
- Consider implementation complexity

## 🔒 Security

- Never commit sensitive data (API keys, passwords)
- Use environment variables for configuration
- Validate all user inputs
- Follow security best practices

## 📞 Getting Help

- Check existing issues and discussions
- Join our team communication channels
- Ask questions in Pull Request comments
- Contact team members directly

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📜 License

By contributing to Fonta AI Study Companion, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to Fonta AI Study Companion!** 🚀

Together, we're building better AI-powered study tools for African students.
