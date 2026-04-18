# ⚽ Skouter – Discovering Football Talent from Rural Communities

Skouter is a platform designed to connect talented football players from rural areas with professional scouts and clubs.

The platform enables parents and young athletes to showcase their skills through profiles, photos, and videos, while allowing scouts to discover talent and send trial invitations.

---

## 🌍 Problem Statement

Many talented football players in rural communities lack visibility and access to professional scouting networks. Traditional scouting methods are limited, geographically biased, and often exclude underrepresented regions.

Skouter bridges this gap by providing a digital platform where talent can be discovered regardless of location.

---

## 🚀 Key Features (MVP)

### 👨‍👩‍👧 Parent & Athlete Registration

* Parents register and manage profiles for athletes under 21
* Athletes (18–21) can self-register
* Secure account creation and role-based access

### 🧑‍🎓 Athlete Profiles

* Personal details (age, location, school/team)
* Football-specific data (position, stats)
* Media uploads:

  * Photos
  * Match/training videos

### 🔍 Scout Discovery

* Browse athletes by:

  * Position
  * Age
  * Location
* View full profiles and performance media

### 📩 Trial Invitations

* Scouts send trial invites
* Parents receive and manage invitations:

  * Accept
  * Decline
* Status tracking for all invites

---

## 🏗️ Tech Stack

* **Backend:** Python, Django
* **API:** Django REST Framework (DRF)
* **Database:** PostgreSQL (recommended)
* **Storage:** Local (MVP) → AWS S3 (future)
* **Authentication:** Django Custom User Model

---

## 📂 Project Structure

```
Skouter/
│
├── accounts/     # User management (parents, athletes, scouts)
├── athletes/     # Athlete profiles
├── scouts/       # Scout profiles & verification
├── invites/      # Trial invitations
├── media/        # Photo & video handling
├── core/         # Shared utilities
│
└── manage.py
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Skouter.git
cd Skouter
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Start Server

```bash
python manage.py runserver
```

---

## 🔐 User Roles

| Role    | Capabilities                                |
| ------- | ------------------------------------------- |
| Parent  | Manage athlete profiles, respond to invites |
| Athlete | (18–21) Manage own profile                  |
| Scout   | Browse players, send trial invites          |
| Admin   | Platform moderation & verification          |

---

## ⚠️ Safety & Trust

Skouter prioritizes child safety and platform integrity:

* No direct communication between scouts and minors
* All interactions go through parents/guardians
* Scout verification system (manual approval in MVP)
* Audit trail for all invitations

---

## 📈 Roadmap

* [ ] Scout verification system
* [ ] Notifications (SMS/Email)
* [ ] Video compression & streaming
* [ ] Mobile app (Android first)
* [ ] AI-based talent highlighting
* [ ] Regional filtering & competitions

---

## 🤝 Contribution

Contributions are welcome. Please fork the repository and submit a pull request.

---

## 📜 License

MIT License

---

## 💡 Vision

To make football talent discovery accessible, inclusive, and unbiased—ensuring that geography is no longer a barrier to opportunity.
