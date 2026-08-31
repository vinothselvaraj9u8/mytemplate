[![MyTemplate](https://user-images.githubusercontent.com/882381/45938197-49cfb880-bf7c-11e8-91ea-94fffd9d054a.png)](https://github.com/sumukh/mytemplate)

# MyTemplate for Flask [![Flask PyTest CI](https://github.com/Sumukh/MyTemplate/actions/workflows/flask-pytest.yml/badge.svg)](https://github.com/Sumukh/MyTemplate/actions/workflows/flask-pytest.yml)

MyTemplate is a scaffold for starting new SaaS applications built using Python and Flask. It takes care of the boilerplate code (like User Registration, OAuth, Teams, and Billing), allowing you to focus on building your application. MyTemplate is built upon best practices for modern Flask applications.

## Features

| Features                              | Status                                       | Details                                                                                    |
| ------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------ |
| User Authentication                   | ✅                                           | User Login, Registration, Forgot Password, Email Confirmation                              |
| OAuth Login                           | ✅                                           | Login or Register with Google, Twitter, Facebook, etc.                                     |
| Teams/Groups                          | ✅                                           | Multi user teams & groups (with Invite Emails)                                             |
| User Export & Deletion Request        | ✅                                           | Allows users to export their data (for GDPR compliance)                                    |
| API                                   | ✅                                           | API (with user tokens) users to access data                                                |
| Stripe Product Checkout               | ✅                                           | One time item purchases with credit cards and receipts (using Stripe)                      |
| Heroku/Docker Deployment              | ✅                                           | Deployment instructions for some platforms. Works on AWS & Google Cloud                    |
| Send Emails                           | ✅                                           | Send email notifications from the application                                              |
| Admin Dashboard                       | ✅                                           | Admin dashboard to edit data                                                               |
| File Uploads                          | ✅                                           | File uploads to cloud storage providers                                                    |
| Basic Test Suite                      | ✅                                           | Starting point for you to build out tests                                                  |
| VS Code Debugger & Editor             | ✅                                           | Configured to make you productive                                                          |
| Tested on Windows 10, OSX, and Ubuntu | ✅                                           | Using Python 3                                                                             |
| SaaS Recurring Billing                | 💲 (Requires purchasing a license to MyTemplate) | Team Billing, Usage Based Billing or Unlimited Plans                                       |
| Commercial Usage                      | 💲 (License Required)                        | Commercial Usage requires a purchased license                                              |
| Video Content                         | 💲                                           | Available as part of [the Fullstack Flask course](https://www.newline.co/fullstack-flask/) |

## How to Buy

| Store                  | Comes With                                                                                                                     | Price                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Fullstack Flask Course | The Fullstack Flask Course & Book, hours of videos explaining how to build a SaaS in Flask, and a single license to MyTemplate Pro | [On Sale (for ~$199) at Newline »](https://www.newline.co/fullstack-flask/) |
| Commercial License     | A license for usage on a single site                                                                                           | [($199) »](https://gumroad.com/l/xFvLo)                                     |

## Setup

Usage of Python 3 is required. It can be installed [on Python.org](https://www.python.org/downloads/)

```
# Optional but recommended:
python3 -m venv env; source env/bin/activate

pip install -r requirements.txt
./manage.py server # or `FLASK_APP=manage flask --debug run`
```

## AI Agent Guide

If you are using an AI coding agent, start with:

- `AGENTS.md` for repo-specific workflow and architecture guidance
- `documentation/AGENT_QUICKSTART.md` for copy-paste setup/test commands
- `make agent-setup`, `make agent-smoke`, and `make agent-test` for standard agent checks

## Development

```
# Development
# If using a virtual env: source env/bin/activate
./manage.py resetdb # to seed data
FLASK_APP=manage flask --debug run

# Go to localhost:5000 in a browser and click on Login
# Login with the following credentials "user@example.com", "test

# Production documentation in the repository.
```

## Testing

Github Actions is configured to run tests and produce code coverage metrics.

To run tests locally, try this command:

```
APPNAME_ENV=test ./manage.py test --coverage
```

### Local Secrets

To configure OAuth login and Stripe billing in development, you will need to set some environment variables. See `.env.local.sample` for an example.

```bash
cp .env.local.sample .env.local
# Edit .env.local with your Stripe & Google test keys
source .env.local
FLASK_APP=manage flask --debug run
```

You may also want to change some of the constants in `appname.constants` and the `services/branding.py` file to change the name of the application in the UI.

## Deployment

MyTemplate is not tied to a specific platform for deployment, but it works well on [Heroku](http://heroku.com) and [Dokku](http://dokku.viewdocs.io/dokku/) with minimal configuration.

It is also designed to work well on other cloud providers such as AWS, Google Cloud, and DigitalOcean.

Documentation is currently provided for installations on Dokku.

## Stripe Webhooks Locally

- Install the [Stripe CLI](https://stripe.com/docs/stripe-cli)
- Login to the Stripe CLI (`stripe login`)
- Run `stripe listen --forward-to localhost:5000/webhooks/stripe`
- Use the webhook secret and configure your app to use it (`export STRIPE_WEBHOOK_SECRET=whsec_...`)
- To replay an event in a seperate console: `stripe events resend evt_XYZ`

## Screenshots

| Screenshot                              | Name                                                    |
| --------------------------------------- | ------------------------------------------------------- |
| Login / Signup / OAuth / Password Reset | ![login](documentation/screenshots/login.png)           |
| Dashboard                               | ![Dashboard](documentation/screenshots/dashboard.png)   |
| Saas Subscription Billing + Console     | ![Billing](documentation/screenshots/billing.png)       |
| Teams                                   | ![Team](documentation/screenshots/team.png)             |
| GDPR/Legal                              | ![GDPR](documentation/screenshots/gdpr.png)             |
| Admin                                   | ![Admin](documentation/screenshots/admin.png)           |
| API Tokens                              | ![API](documentation/screenshots/api.png)               |
| Delayed Jobs                            | ![Jobs](documentation/screenshots/jobs.png)             |
| Emails                                  | ![Emails](documentation/screenshots/email.png)          |
| File Uploads                            | ![Files](documentation/screenshots/file-uploads.png)    |
| Stripe Customer Portal Integration      | ![Stripe](documentation/screenshots/stripe-console.png) |

## License

This is a commercial product. You may purchase a license for commercial use at [MyTemplate Website](https://mytemplate.sumukh.me)

Here's a summary:

| Features                                     | MyTemplate         | (License) MyTemplate Premium |
| -------------------------------------------- | -------------- | ------------------------ |
| Cost                                         | Free           | $199 per site            |
| Private Non Commercial Use                   | ✅             | ✅                       |
| Commercial Use                               | No             | ✅                       |
| Ability to remove "Powered by MyTemplate" footer | No             | ✅                       |
| Video Tutorials                              | No             | ✅                       |
| Re-license                                   | No             | Contact us               |
| Support                                      | No             | No                       |
| Warranty                                     | Provided As-is | Provided As-is           |
| Refunds                                      | N/A            | 30 Day                   |

You can purchase a license at the [MyTemplate Store](https://gumroad.com/l/xFvLo) or on [Newline as part of the Fullstack Flask course](https://www.newline.co/fullstack-flask/)

For more detailed license information see LICENSE.md

## Credits

Design elements from [tabler](https://github.com/tabler/tabler) & Bootstrap 4.

Built off of [Flask Foundation](https://jackstouffer.github.io/Flask-Foundation/) and the [bootstrapy project](https://github.com/kirang89/bootstrapy)

### Extra Reading

Only building out an API using Flask?

- Use [create-flask-api](https://github.com/Sumukh/create-flask-api)

**Course: [Fullstack Flask: Build a SaaS using Python and Flask](https://www.newline.co/fullstack-flask/)**

Best practices List:

- [Larger Applications With Flask](http://flask.pocoo.org/docs/patterns/packages/).
- [Creating Websites With Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)
- [Getting Bigger With Flask](http://maximebf.com/blog/2012/11/getting-bigger-with-flask/)
- [Miguel Grinberg's Blog](https://blog.miguelgrinberg.com/category/Python)

## Assessment Notes: Running the App and Checks Locally

This section documents the work done for the DevOps Support and QA Engineer take-home assessment.

### Running the app locally

```bash
pip install -r requirements.txt
python manage.py initdb    # first time only, creates the database tables
python manage.py server    # starts the dev server at http://127.0.0.1:5000
```

### Running the full quality pipeline

A `Makefile` is provided with the following targets:

```bash
make test        # runs the full pytest suite, outputs JUnit XML to reports/junit.xml
make coverage     # runs tests with coverage, outputs XML + HTML to reports/coverage/
make lint         # runs Ruff static analysis, outputs JSON to reports/ruff-report.json
make security     # runs Bandit security scan, outputs JSON to reports/bandit-report.json
make reports      # runs all of the above in sequence
make clean        # removes generated reports and caches
```

All reports are written to the `reports/` directory after running `make reports`.

### Test suite

- 105 tests total: the pre-existing starter-project test suite plus two new tests added for this
  assessment (`tests/test_main.py` for a backend pytest check on the homepage/terms routes, and
  `tests/test_ui.py` for a Playwright UI check that the homepage renders with MyTemplate branding).
- Current coverage: ~86%.
- The UI test (`tests/test_ui.py`) requires the Flask dev server to be running at
  `http://127.0.0.1:5000` before it's run.

### Known limitations

- The hero screenshot image (`demo-1.png`) on the landing page still shows "ignite" branding baked
  into the image pixels from the original starter project. This is a static screenshot, not live
  text, so it was left as-is to stay in scope rather than editing image assets.
- A typo'd brand reference ("Ingite" instead of "Ignite") was found and fixed in `store.py` during
  manual review, since it wasn't caught by the initial case-sensitive find/replace pass.
- Ruff reports 44 pre-existing style issues in the original starter codebase (103 additional issues
  were auto-fixed). These are reported by `make lint` but do not fail the build, since fixing
  pre-existing issues in unrelated legacy code was out of scope for this assessment.
- Bandit reports 0 security issues; one finding (weak MD5 usage for a non-cryptographic salt) was
  fixed by adding `usedforsecurity=False`.
- The GitHub Actions workflow (`.github/workflows/flask-pytest.yml`) has been extended to run the
  full `make reports` pipeline, including starting the Flask server so the Playwright UI test can
  run in CI. The Makefile and all report generation have been fully verified locally; CI was tested
  but not fully green at time of submission — see repository Actions tab for current status.

## Assessment Notes: Running the App and Checks Locally

This section documents the work done for the DevOps Support and QA Engineer take-home assessment.

### Running the app locally

```bash
pip install -r requirements.txt
python manage.py initdb    # first time only, creates the database tables
python manage.py server    # starts the dev server at http://127.0.0.1:5000
```

### Running the full quality pipeline

A `Makefile` is provided with the following targets:

```bash
make test        # runs the full pytest suite, outputs JUnit XML to reports/junit.xml
make coverage     # runs tests with coverage, outputs XML + HTML to reports/coverage/
make lint         # runs Ruff static analysis, outputs JSON to reports/ruff-report.json
make security     # runs Bandit security scan, outputs JSON to reports/bandit-report.json
make reports      # runs all of the above in sequence
make clean        # removes generated reports and caches
```

All reports are written to the `reports/` directory after running `make reports`.

### Test suite

- 105 tests total: the pre-existing starter-project test suite plus two new tests added for this
  assessment (`tests/test_main.py` for a backend pytest check on the homepage/terms routes, and
  `tests/test_ui.py` for a Playwright UI check that the homepage renders with MyTemplate branding).
- Current coverage: ~86%.
- The UI test (`tests/test_ui.py`) requires the Flask dev server to be running at
  `http://127.0.0.1:5000` before it's run.

### Known limitations

- The hero screenshot image (`demo-1.png`) on the landing page still shows "ignite" branding baked
  into the image pixels from the original starter project. This is a static screenshot, not live
  text, so it was left as-is to stay in scope rather than editing image assets.
- A typo'd brand reference ("Ingite" instead of "Ignite") was found and fixed in `store.py` during
  manual review, since it wasn't caught by the initial case-sensitive find/replace pass.
- Ruff reports 44 pre-existing style issues in the original starter codebase (103 additional issues
  were auto-fixed). These are reported by `make lint` but do not fail the build, since fixing
  pre-existing issues in unrelated legacy code was out of scope for this assessment.
- Bandit reports 0 security issues; one finding (weak MD5 usage for a non-cryptographic salt) was
  fixed by adding `usedforsecurity=False`.
- The GitHub Actions workflow (`.github/workflows/flask-pytest.yml`) has been extended to run the
  full `make reports` pipeline, including starting the Flask server so the Playwright UI test can
  run in CI. The Makefile and all report generation have been fully verified locally.
