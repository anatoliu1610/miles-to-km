# Miles to Kilometers Converter

A simple, clean web app to convert miles to kilometers. Deploys to free hosting platforms in minutes.

## Features
- Web form with instant conversion
- REST API (`POST /convert`)
- Health check endpoint (`/health`)
- Mobile-friendly responsive UI
- Input validation (positive numbers only)
- No external dependencies beyond Flask

## Quick Start

### Local Development

1. **Clone and setup:**
```bash
cd miles-to-km
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run the app:**
```bash
FLASK_DEBUG=true python app.py
```

3. **Open** http://localhost:5000 in your browser.

### API Usage

```bash
# Convert 10 miles to km
curl -X POST http://localhost:5000/convert \
  -H "Content-Type: application/json" \
  -d '{"miles": 10}'

# Response
{
  "miles": 10,
  "kilometers": 16.0934,
  "unit": "km"
}
```

## Deploy to Free Hosting

### Option 1: Render (Recommended)

1. Push this folder to a **GitHub repository**.
2. Go to [render.com](https://render.com) → **New Web Service**.
3. Connect your GitHub repo.
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free
5. Click **Create Web Service**. Deploy takes ~2 minutes.
6. Your live URL: `https://your-app.onrender.com`

### Option 2: Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create miles-to-km-converter

# Push to deploy
git push heroku main

# Open in browser
heroku open
```

### Option 3: Railway

1. Install Railway CLI: `npm i -g railway`
2. `railway login`
3. `railway init` → choose this directory
4. `railway up`

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Bind port (set by platform) |
| `FLASK_DEBUG` | `False` | Enable debug mode (dev only) |
| `SECRET_KEY` | (none) | Flask secret key (optional) |

---

## Testing

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/

# Or use Python's unittest
python -m unittest discover tests
```

---

## Project Structure

```
miles-to-km/
├── app.py            # Flask application (backend + frontend)
├── requirements.txt  # Python dependencies
├── Procfile          # Heroku/Render procfile
├── runtime.txt       # Python version hint
├── .env.example      # Environment template
├── .gitignore        # Git ignore rules
├── README.md         # This file
└── tests/
    └── test_api.py   # API tests
```

---

## Customization

- **Change conversion factor**: Edit `1.60934` in `app.py`
- **Add more units**: Extend the `/convert` endpoint
- **Styling**: Modify the CSS in the `HTML` string in `app.py`
- **Separate frontend**: Move HTML to templates/index.html

---

## License

MIT – feel free to use commercially.

---

## Support

Open an issue or ask me (Liza) for help! 🔧