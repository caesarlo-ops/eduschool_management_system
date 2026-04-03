# Production Deployment Checklist for KDF Finance Solutions

## Domain: kdfinancesolutions.co.zw
## IP: 185.150.189.233

---

## ✅ STEP 1: Generate New SECRET KEY

**IMPORTANT:** Before deploying, generate a new secret key!

Run this command in your terminal:
```powershell
cd "c:\Users\USER\OneDrive\Desktop\School Manangement\school_management"
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key and replace it in `settings.py` line 12.

---

## ✅ STEP 2: Database Setup on Production Server

1. **Install PostgreSQL** on your server (if not already installed)
2. **Create database and user:**
   ```sql
   CREATE DATABASE school_management;
   CREATE USER postgres WITH PASSWORD 'xavier';
   GRANT ALL PRIVILEGES ON DATABASE school_management TO postgres;
   ```

3. **Update DATABASES settings** if the production database credentials are different

---

## ✅ STEP 3: Install Dependencies

On your production server:
```bash
pip install -r requirements.txt
```

---

## ✅ STEP 4: Collect Static Files

On your production server:
```bash
python manage.py collectstatic --noinput
```

This will gather all static files into the `staticfiles` directory.

---

## ✅ STEP 5: Run Database Migrations

On your production server:
```bash
python manage.py migrate
```

---

## ✅ STEP 6: Create Superuser (Optional but Recommended)

On your production server:
```bash
python manage.py createsuperuser
```

---

## ✅ STEP 7: Configure Web Server (Apache/Nginx)

### Option A: Using Nginx + Gunicorn (Recommended)

**Install Gunicorn:**
```bash
pip install gunicorn
```

**Nginx Configuration Example** (`/etc/nginx/sites-available/school_management`):
```nginx
server {
    listen 80;
    server_name kdfinancesolutions.co.zw www.kdfinancesolutions.co.zw;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Run with Gunicorn:**
```bash
gunicorn --workers 3 --bind 127.0.0.1:8000 config.wsgi:application
```

### Option B: Using Apache + mod_wsgi

**Install mod_wsgi:**
```bash
pip install mod_wsgi
mod_wsgi-express module-config
```

**Apache Configuration Example:**
```apache
<VirtualHost *:80>
    ServerName kdfinancesolutions.co.zw
    
    WSGIDaemonProcess school_management pythonpath=/path/to/your/project
    WSGIProcessGroup school_management
    WSGIScriptAlias / /path/to/your/project/config/wsgi.py
    
    Alias /static /path/to/your/project/staticfiles
    <Directory /path/to/your/project/staticfiles>
        Require all granted
    </Directory>
    
    <Directory /path/to/your/project/config>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>
```

---

## ✅ STEP 8: SSL/HTTPS Setup (HIGHLY RECOMMENDED)

Use Let's Encrypt for free SSL certificate:

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d kdfinancesolutions.co.zw -d www.kdfinancesolutions.co.zw
```

After SSL setup, update `settings.py`:
- Set `CSRF_COOKIE_SECURE = True`
- Set `SESSION_COOKIE_SECURE = True`

---

## ✅ STEP 9: Firewall Configuration

Make sure these ports are open:
- Port 80 (HTTP)
- Port 443 (HTTPS) - if using SSL

---

## ✅ STEP 10: Test Your Deployment

1. Access your site: `http://kdfinancesolutions.co.zw`
2. Test login functionality
3. Test all major features
4. Check browser console for errors

---

## 🔒 Security Reminders

1. ✅ Change the SECRET_KEY (Step 1)
2. ✅ Keep DEBUG = False
3. ✅ Use strong database passwords
4. ✅ Enable HTTPS/SSL as soon as possible
5. ✅ Regular backups of your database
6. ✅ Keep Django and dependencies updated

---

## 📝 Environment Variables (Best Practice)

Consider using environment variables for sensitive data:

1. **Install python-decouple:**
   ```bash
   pip install python-decouple
   ```

2. **Create `.env` file:**
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   DB_PASSWORD=your-db-password
   ```

3. **Update settings.py to use decouple**

---

## 🆘 Troubleshooting

**Issue: Static files not loading**
- Make sure you ran `collectstatic`
- Check web server configuration points to correct static directory

**Issue: Database connection error**
- Verify PostgreSQL is running
- Check database credentials in settings.py
- Ensure database exists and user has permissions

**Issue: CSRF errors**
- Check CSRF_TRUSTED_ORIGINS includes your domain
- Verify cookies are being set correctly

**Issue: Permission denied errors**
- Check file permissions on the server
- Ensure web server user can read project files

---

## 📞 Next Steps After Deployment

1. Monitor your application logs
2. Set up regular database backups
3. Configure error logging
4. Set up monitoring/alerts
5. Test backup restoration procedure

---

Good luck with your deployment! 🚀
