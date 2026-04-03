# Production Deployment Script for School Management System
# Run this on your production server after uploading your project

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "School Management System - Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Install/Update dependencies
Write-Host "[1/5] Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
Write-Host ""

# Step 2: Collect static files
Write-Host "[2/5] Collecting static files..." -ForegroundColor Yellow
python manage.py collectstatic --noinput
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to collect static files!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Static files collected successfully" -ForegroundColor Green
Write-Host ""

# Step 3: Run database migrations
Write-Host "[3/5] Running database migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to run migrations!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Database migrations completed successfully" -ForegroundColor Green
Write-Host ""

# Step 4: Check system
Write-Host "[4/5] Running system check..." -ForegroundColor Yellow
python manage.py check --deploy
Write-Host ""

# Step 5: Create superuser prompt
Write-Host "[5/5] Would you like to create a superuser (admin account)?" -ForegroundColor Yellow
$response = Read-Host "Enter 'y' for yes or 'n' for no"
if ($response -eq 'y' -or $response -eq 'Y') {
    python manage.py createsuperuser
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host "Deployment completed successfully! ✓" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Configure your web server (Gunicorn/Apache)" -ForegroundColor White
Write-Host "2. Set up SSL certificate for HTTPS" -ForegroundColor White
Write-Host "3. Access your site at http://kdfinancesolutions.co.zw" -ForegroundColor White
Write-Host ""
Write-Host "IMPORTANT: Don't forget to update your SECRET_KEY in settings.py!" -ForegroundColor Red
Write-Host ""
