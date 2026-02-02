# Eraser
**URL:** https://app.eraser.io/workspace/KuPhKKF9Cnq19Jr0BMBd
**Page Title:** Dionysus — Eraser
--------------------


## Dionysus: Technical Documentation

## 1. Executive Summary

Dionysus is an AI-powered GitHub assistant SaaS platform designed to help developers code more efficiently and quickly. It provides code suggestions, repository analysis, and collaborative tools through a modern web application built with Next.js, React, and TypeScript.

### Core Technology Stack

- Frontend : Next.js 15 with App Router, React 19, TypeScript
- Styling : TailwindCSS with shadcn/ui components
- Authentication : Clerk with custom OAuth flow
- Backend : Next.js API routes, tRPC, Prisma ORM
- Database : PostgreSQL with pgvector extension for vector embeddings
- AI Integration : Google Gemini Pro, AssemblyAI
- Payment Processing : Stripe
- Deployment : Vercel
- Monitoring : Sentry, Arcjet
- Other Key Technologies : Stream Chat, Redis, Cloudinary

### System Architecture Overview

Dionysus follows a modern full-stack architecture with server components for initial rendering, client components for interactivity, and API routes for data operations. The system is designed to be scalable, secure, and maintainable with clear separation of concerns.

## 2. System Architecture

### 2.1 Frontend Architecture

Dionysus uses Next.js App Router, organizing routes as filesystem-based components within the app directory. The application uses both server and client components strategically:
- Server Components : Used for data fetching and initial rendering
- Client Components : Used for interactive elements and state management
Key directories include:
- (protected): Routes requiring authentication
- admin: Admin-only routes with server-side validation
- api: API endpoints
- components: Reusable UI components
Components are organized by functionality:
- Layout Components : Define page structure (e.g., layout.tsx)
- Page Components : Main content for routes (e.g., page.tsx)
- UI Components : Reusable interface elements (e.g., StatusChart.tsx)
- Feature Components : Domain-specific components (e.g., CommunitySidebar.tsx)
The application uses a combination of:
- React Context API for global state (theme, user settings)
- React hooks for local component state
- Server components for initial data fetching
- tRPC for typed API interactions
Example from AuthCallbackPage.tsx :
- Server Components : Direct database access via Prisma
- API Routes : RESTful endpoints for public/external interfaces
- tRPC : Type-safe RPC for internal client-server communication
- SWR/React Query : For client-side data fetching with caching
Dionysus uses Shadcn/UI, a collection of accessible and customizable components built on top of Tailwind CSS. Components are styled using utility classes and customized through a well-defined theming system.

### 2.2 Backend Architecture

The backend is composed of:
- Next.js API Routes ( /src/app/api/* ): RESTful endpoints for external services integration Public endpoints for unauthenticated access Webhook handlers (Stripe, GitHub)
- RESTful endpoints for external services integration
- Public endpoints for unauthenticated access
- Webhook handlers (Stripe, GitHub)
- tRPC Routes (route.ts): Type-safe API for frontend-backend communication Protected routes with automatic type checking Organized by domain (projects, users, analytics)
- Type-safe API for frontend-backend communication
- Protected routes with automatic type checking
- Organized by domain (projects, users, analytics)
- Server Actions : Form submissions Database mutations Authentication operations
- Form submissions
- Database mutations
- Authentication operations
Core entities in the Prisma schema include:
- User : Stores user profile information Links to Clerk authentication Tracks credits and subscription status
- Stores user profile information
- Links to Clerk authentication
- Tracks credits and subscription status
- Project : Represents GitHub repositories Contains metadata and analysis results Links to users through UserToProject
- Represents GitHub repositories
- Contains metadata and analysis results
- Links to users through UserToProject
- SourceCodeEmbedding : Stores vector embeddings for code analysis Enables semantic search capabilities Links to projects
- Stores vector embeddings for code analysis
- Enables semantic search capabilities
- Links to projects
- Meeting : Stores meeting transcripts and recordings AI-analyzed content and summaries User participation data
- Stores meeting transcripts and recordings
- AI-analyzed content and summaries
- User participation data
- StripeTransaction : Payment history Credit purchases Subscription events
- Payment history
- Credit purchases
- Subscription events
Authentication is implemented using Clerk:
- Client-Side : ﻿ ClerkProviderWithTheme wraps the application Custom OAuth callback handling via /auth-callback Theme-aware authentication UI
- ﻿ ClerkProviderWithTheme wraps the application
- Custom OAuth callback handling via /auth-callback
- Theme-aware authentication UI
- Server-Side : Middleware validation for protected routes Role-based access control for admin routes JWT validation for API requests
- Middleware validation for protected routes
- Role-based access control for admin routes
- JWT validation for API requests
- Admin Authentication : Server-side validation in layout.tsx Email and user ID verification Middleware checks for admin routes
- Server-side validation in layout.tsx
- Email and user ID verification
- Middleware checks for admin routes
The application uses a sophisticated middleware chain for request processing:
- Clerk Authentication : Validates user sessions
- Route Matching : Determines public vs. protected routes
- Arcjet Security : Applies rate limiting and bot detection
- Geolocation Filtering : Blocks traffic from restricted countries
- Custom Processing : Handles specific request types
From middleware.ts:
- GitHub API : Repository access and analysis Commit history retrieval Code embedding generation
- Repository access and analysis
- Commit history retrieval
- Code embedding generation
- Stripe : Payment processing Subscription management Webhook handling for events
- Payment processing
- Subscription management
- Webhook handling for events
- AI Services : Google Gemini Pro for code analysis AssemblyAI for speech-to-text Vector embeddings for semantic search
- Google Gemini Pro for code analysis
- AssemblyAI for speech-to-text
- Vector embeddings for semantic search

### 2.3 DevOps Architecture

The application is deployed on Vercel with:
- CI/CD Workflow : GitHub Actions for automated testing Husky pre-commit hooks for code quality Commitlint for commit message validation
- GitHub Actions for automated testing
- Husky pre-commit hooks for code quality
- Commitlint for commit message validation
- Environment Management : Doppler for environment variable management Docker containerization for consistent environments Separate staging and production deployments
- Doppler for environment variable management
- Docker containerization for consistent environments
- Separate staging and production deployments
- Monitoring and Alerting : Sentry for error tracking and performance monitoring Custom status page with uptime monitoring Arcjet for security monitoring
- Sentry for error tracking and performance monitoring
- Custom status page with uptime monitoring
- Arcjet for security monitoring

### 2.4 Security Architecture

- Clerk Integration : Multi-provider OAuth (Google, GitHub) Email/password authentication Session management and JWT handling
- Multi-provider OAuth (Google, GitHub)
- Email/password authentication
- Session management and JWT handling
- Authorization Model : Role-based access (admin, user) Resource-level permissions Project-specific access control
- Role-based access (admin, user)
- Resource-level permissions
- Project-specific access control
- API Security : Arcjet rate limiting Bot detection and blocking Input validation and sanitization
- Arcjet rate limiting
- Bot detection and blocking
- Input validation and sanitization
- Content Security Policy : Strict CSP headers XSS protection CSRF prevention
- Strict CSP headers
- XSS protection
- CSRF prevention
From middleware.ts:

## 3. Core Module Documentation

### 3.1 API Routes

Purpose : Provides system uptime and health metrics for monitoring.
HTTP Methods : GET, HEAD, OPTIONS
Request Parameters :
- Headers: x-uptimerobot-monitor-id (optional for UptimeRobot monitoring)
Response Format :
Implementation Details :
- Checks for required environment variables
- Validates Clerk service availability
- Fetches and processes monitor data
- Formats response based on request headers
Error Handling :
- 500: Missing environment variables
- 500: Clerk unavailable
- 400: Invalid request parameters
Security Considerations :
- Public endpoint without authentication
- Rate limited via Arcjet
- Limited response data for security
Purpose : Handles Stripe webhook events for payment processing.
HTTP Methods : POST
Request Parameters :
- Body: Stripe webhook event payload
- Headers: stripe-signature for verification
Implementation Details :
- Verifies webhook signature using Stripe SDK
- Processes different event types (checkout.session.completed, etc.)
- Updates user credits and subscription status
- Records transactions in the database
Error Handling :
- 400: Invalid signature
- 400: Missing event type
- 500: Database operation failure
Security Considerations :
- Signature verification for webhook authenticity
- Idempotency handling to prevent duplicate processing
- No authentication required (Stripe-specific endpoint)

### 3.2 Middleware

Purpose : Handles authentication, rate limiting, and request processing.
Route Matching Logic :
- Public routes: Sign-in, sign-up, landing page, docs
- Protected routes: Dashboard, settings, projects
- Admin routes: Admin dashboard, user management
Authentication Flow :
Rate Limiting Strategy :
- Arcjet integration with fixed window approach
- 80 requests per 60 seconds limit
- Bot detection with an allowlist for search engines
Geolocation Processing :
- Country blocking for specific regions
- Redirect logic for blocked users
Security Headers :
- Content Security Policy configuration
- CORS settings
- XSS protection measures

### 3.3 Core Components

File Path : StatusChart.tsx
Purpose : Visualizes system uptime and performance metrics
Props Interface :
Data Processing :
- Uptime calculation algorithm
- Response time formatting
- Time series data generation
Chart Rendering :
Utility Functions :
- ﻿ formatUptime : Formats numeric uptime percentage values
- ﻿ formatResponseTime : Converts milliseconds to a human-readable format
- ﻿ getColorForStatus : Determines color based on status
File Path : page.tsx
Purpose : Custom loading page for OAuth authentication flow
State Management :
- Loading state management
- Animation for loading dots
- Authentication status tracking
Authentication Logic :
UI Rendering :
- Loading animation with dots
- Progress indicator
- Logo display
- Responsive layout for mobile and desktop

## 4. Database Schema Documentation

### 4.1 Core Entities

- Authentication Integration : Links to Clerk via emailAddress
- Subscription Tracking : isPro Flag for subscription status
- Credit System : credits For usage tracking
- Relationships : Projects, questions, transactions
- GitHub Integration : Links to repositories via githubUrl
- Soft Delete : deletedAt For non-destructive removal
- Access Control : Creator ID and user relationships
- Analysis Data : Commits, embeddings, and questions
- Vector Database : Stores code embeddings for AI analysis
- Project Association : Links to parent project
- Content Storage : Original code and AI-generated summary

### 4.2 Entity Relationships

Key relationships in the schema:
User to Project (Many-to-Many):
Project to Meeting (One-to-Many):
User to Transaction (One-to-Many):

## 5. Authentication & Authorization System

### 5.1 Clerk Integration

Configuration :
Custom OAuth Flow :
- Custom navigation handling in ClerkProvider
- Auth callback page for improved UX
- Theme-aware authentication UI

### 5.2 Role-Based Access Control

Admin Access Control :
Resource-Level Permissions :
- Project-specific access control
- Creator vs. collaborator permissions
- Feature access based on subscription tier

### 5.3 API Security

Authentication Mechanisms :
- JWT validation for API routes
- Session validation in middleware
- tRPC protected procedures
Rate Limiting :
Input Validation :
- Zod schema validation for request data
- Type checking with TypeScript
- Sanitization for user-generated content

## 6. Infrastructure & Deployment

### 6.1 Docker Configuration

Dockerfile :
Environment Management :
- Doppler integration for secrets management
- External Neon PostgreSQL database
- Runtime environment configuration

### 6.2 CI/CD Pipeline

GitHub Actions :
- Automated testing on pull requests
- Linting and type checking
- Build validation
Commit Quality :
Deployment Strategy :
- Vercel for production deployment
- Preview deployments for pull requests
- Environment-specific configurations

### 6.3 Monitoring & Alerting

Error Tracking :
Status Monitoring :
- Custom status page with uptime tracking
- Service health checks
- Incident reporting and history
Performance Monitoring :
- Vercel Analytics integration
- Custom performance metrics
- Client-side performance tracking

## 7. AI & ML Implementation

### 7.1 Google Gemini Pro Integration

Purpose : Code analysis, summarization, and question answering
Implementation :
Features :
- Code understanding and explanation
- Bug detection and fixing
- Best practice recommendations

### 7.2 AssemblyAI Integration

Purpose : Transcription and analysis of meeting recordings
Implementation :
- Audio processing pipeline
- Speaker diarization
- Transcription, storage, and retrieval
Features :
- Meeting summaries
- Action item extraction
- Searchable transcripts

### 7.3 Vector Embeddings

Purpose : Semantic search and code understanding
Implementation :
- pgvector extension for PostgreSQL
- Embedding generation for code files
- Similarity search functionality
Features :
- Code search by natural language
- Related code identification
- Contextual recommendations

## 8. External Integrations

### 8.1 GitHub API

Purpose : Repository access and analysis
Implementation :
- Repository cloning and scanning
- Commit history retrieval
- Code structure analysis
Features :
- Automatic code scanning
- Repository insights
- Collaboration tracking

### 8.2 Stripe Integration

Purpose : Payment processing and subscription management
Implementation :
- Checkout sessions for credit purchases
- Subscription handling for Pro tier
- Webhook processing for events
Features :
- Credit-based billing model
- Subscription management
- Payment history tracking

### 8.3 Stream Chat

Purpose : Real-time chat and collaboration
Implementation :
- Channel creation and management
- User authentication with Stream
- Real-time messaging
Features :
- Project-specific chat channels
- Direct messaging
- File sharing and code snippets

## 9. Performance Optimization

### 9.1 Frontend Performance

Code Splitting :
- Route-based splitting with Next.js
- Dynamic imports for heavy components
- Component-level code splitting
Image Optimization :
- Next.js Image component usage
- Responsive image loading
- Lazy loading for off-screen images
Rendering Strategies :
- Server components for static content
- Client components for interactive elements
- Partial hydration patterns

### 9.2 Backend Performance

Database Optimization :
- Efficient indexing strategy
- Query optimization with Prisma
- Connection pooling
Caching Strategy :
- Redis for session and data caching
- SWR for client-side data caching
- Static generation for stable content
Async Processing :
- Background jobs for heavy tasks
- Batch processing, where applicable
- Rate limiting for API-heavy operations

## 10. Security Implementation

### 10.1 Data Protection

Encryption :
- Secure password hashing
- HTTPS everywhere
- Environment variable encryption
PII Handling :
- Minimization of personal data collection
- Secure storage of user information
- Access controls for sensitive data
Data Retention :
- Clear retention policies
- Secure deletion mechanisms
- Data minimization practices

### 10.2 Content Security Policy

CSP Headers :
XSS Protection :
- Content sanitization
- Script execution controls
- Input validation
CSRF Prevention :
- Token validation
- SameSite cookie policies
- Origin checking

## 11. Development Workflow

### 11.1 Local Development

Setup Requirements :
- Node.js v20+
- PostgreSQL with pgvector
- Redis (optional)
- Environment variables configuration
Development Commands :

### 11.2 Code Quality Tools

Linting and Formatting :
Git Hooks :
- Husky for pre-commit hooks
- Commitlint for commit message validation
- Lint-staged for staged file validation
TypeScript Configuration :
- Strict type checking
- Path aliases for imports
- Type generation for external APIs

## 12. Appendices

### 12.1 Environment Variables

Core Variables :
- ﻿ DATABASE_URL : PostgreSQL connection string
- ﻿ CLERK_SECRET_KEY : Clerk authentication secret
- ﻿ STRIPE_SECRET_KEY : Stripe API key
- ﻿ GEMINI_API_KEY : Google Gemini API key
- ﻿ UPTIME_ROBOT_API_KEY : Monitoring API key
- ﻿ ADMIN_EMAIL : Administrator email address
- ﻿ ADMIN_USER_ID : Administrator user ID
Development Variables :
- ﻿ NODE_OPTIONS : Node.js memory configuration
- ﻿ NEXT_PUBLIC_BASE_URL : Application base URL
- ﻿ REDIS_URL : Redis connection string

### 12.2 Tech Stack Reference

Core Technologies :
- Next.js 15.4.5
- React 19.1.1
- TypeScript 5.8.3
- PostgreSQL with pgvector
- Prisma 6.11.0
- TailwindCSS 3.4.3
Authentication & Security :
- Clerk for authentication
- Arcjet for rate limiting and security
- Content Security Policy implementation
UI Components :
- shadcn/ui component library
- Radix UI primitives
- Lucide React icons
- TailwindCSS for styling
State Management & Data Fetching :
- React Context API
- React Query / TanStack Query
- tRPC for type-safe APIs
AI & ML :
- Google Generative AI (Gemini Pro)
- AssemblyAI for audio processing
- Vector embeddings for semantic search
DevOps & Monitoring :
- Vercel for hosting
- Docker for containerization
- Sentry for error tracking
- Custom status monitoring
Payment Processing :
- Stripe for payments
- Custom credit system
- Subscription management

### 12.3 Coding Standards

File Organization :
- Route-based component organization
- Feature folders for related components
- Shared components in /components
- Utility functions in /lib
Naming Conventions :
- PascalCase for React components
- camelCase for variables and functions
- kebab-case for file names
- UPPER_CASE for constants
Component Structure :
- Props interface defined at the top
- Hooks and state declarations next
- Helper functions before render
- JSX returned at the end
State Management Patterns :
- Local state with useState
- Context for shared state
- Props for component-specific data
- Server state with React Query

## Conclusion

Dionysus is a sophisticated, enterprise-grade GitHub analytics and collaboration platform built with modern web technologies. The application leverages AI capabilities to provide intelligent insights into code repositories, facilitates team collaboration, and offer powerful developer tools.
The architecture adheres to best practices for security, scalability, and maintainability, with a clear separation of concerns and typed interfaces throughout. The use of Next.js App Router provides excellent performance and developer experience, while integrations with services like Clerk, Stripe, and Google Gemini AI extend the platform's capabilities.
This documentation serves as a comprehensive guide for developers working on the Dionysus codebase, providing detailed explanations of all major components, architecture decisions, and implementation details.

--------------------