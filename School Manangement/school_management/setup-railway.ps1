# Railway Deployment - Quick Start Script
# This script automates the Git setup process for Railway deployment

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Railway Deployment Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "[Step 1/6] Checking if Git is installed..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git from: https://git-scm.com/downloads" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installation, restart PowerShell and run this script again." -ForegroundColor Cyan
    exit 1
}
Write-Host ""

# Check if already a Git repository
Write-Host "[Step 2/6] Checking Git repository status..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "✓ Git repository already initialized" -ForegroundColor Green
} else {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Git repository initialized successfully" -ForegroundColor Green
    } else {
        Write-Host "✗ Failed to initialize Git repository" -ForegroundColor Red
        exit 1
    }
}
Write-Host ""

# Add all files
Write-Host "[Step 3/6] Adding files to Git..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ All files staged successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to add files" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Commit changes
Write-Host "[Step 4/6] Creating Git commit..." -ForegroundColor Yellow
$commitMessage = "Railway deployment ready - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git commit -m $commitMessage
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Changes committed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠ No changes to commit or commit failed" -ForegroundColor Yellow
}
Write-Host ""

# Check for GitHub remote
Write-Host "[Step 5/6] Checking GitHub configuration..." -ForegroundColor Yellow
$remoteUrl = git remote get-url origin 2>$null
if ($remoteUrl) {
    Write-Host "✓ GitHub remote already configured: $remoteUrl" -ForegroundColor Green
} else {
    Write-Host "GitHub remote not configured yet." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Next steps to configure GitHub:" -ForegroundColor Cyan
    Write-Host "1. Go to https://github.com and create a new repository" -ForegroundColor White
    Write-Host "2. Name it: school-management" -ForegroundColor White
    Write-Host "3. Copy the repository URL" -ForegroundColor White
    Write-Host "4. Run this command (replace YOUR_USERNAME with your GitHub username):" -ForegroundColor White
    Write-Host ""
    Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/school-management.git" -ForegroundColor Gray
    Write-Host ""
}
Write-Host ""

# Display summary
Write-Host "[Step 6/6] Deployment Summary" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ Your project is now Railway-ready!" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Push to GitHub (if remote is configured):" -ForegroundColor White
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Deploy on Railway:" -ForegroundColor White
Write-Host "   - Go to https://railway.app" -ForegroundColor Gray
Write-Host "   - Click 'New Project'" -ForegroundColor Gray
Write-Host "   - Select 'Deploy from GitHub repo'" -ForegroundColor Gray
Write-Host "   - Choose your repository" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Add PostgreSQL database in Railway dashboard" -ForegroundColor White
Write-Host ""
Write-Host "4. Set environment variables in Railway:" -ForegroundColor White
Write-Host "   SECRET_KEY = -rv^+)j8_dl$u)o71zslaygb+pghvlxqih5gcxp706n=xrmu1f" -ForegroundColor Gray
Write-Host "   DEBUG = False" -ForegroundColor Gray
Write-Host "   ALLOWED_HOSTS = kdfinancesolutions.co.zw,www.kdfinancesolutions.co.zw,185.150.189.233,your-railway-url.railway.app" -ForegroundColor Gray
Write-Host ""
Write-Host "📖 For detailed instructions, see RAILWAY_DEPLOYMENT.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Good luck with your deployment! 🚀" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
