# SpringRocket
A Python CLI tool to quickly scaffold Java Spring Boot microservices with optional Docker, PostgreSQL, and SaaS-ready billing endpoints. Perfect for small teams or open-source projects that want a working microservice boilerplate in seconds.

Perfect! Since we now have a fully working CLI generator **“SpringRocket”** with correct Maven structure, Docker support, billing placeholders, and fully generated README for each service, here’s a **polished, updated `README.md` for your CLI repo**:

---

# **Universal Microservice CLI — SpringRocket 🚀**

**SpringRocket** is the name of this CLI because it lets you **launch Spring Boot microservices at rocket speed**.

We wanted a name that captures the thrill of taking an idea and having a fully working microservice ready to run in **seconds**. With SpringRocket, you don’t wait — you scaffold, run, and see your service in action almost instantly. Think of it as your personal launchpad for microservices and SaaS-ready applications.

---

## **Features**

* Generate a **Spring Boot microservice** with REST endpoints
* Fully **Maven-compliant project structure** (`src/main/java`, `src/main/resources`)
* Optional **Dockerfile** for containerization
* Optional **PostgreSQL DB config** (`application.properties`)
* Optional **BillingController** with **Stripe/PayPal placeholders**
* Automatic **README.md** inside generated service
* Produces **ready-to-run JAR** (`target/<ServiceName>.jar`) for Docker or local execution
* Quick scaffold for **SaaS-style microservices**

---

## **Installation**

```bash
git clone <repo-url>
cd universal-microservice-cli
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

---

## **Usage**

```bash
python cli.py create-service <ServiceName> [OPTIONS]
```

**Options:**

* `--docker` → Add Dockerfile
* `--db` → Add PostgreSQL configuration
* `--billing` → Add BillingController (Stripe & PayPal placeholders)

**Example:**

```bash
python cli.py create-service UserService --docker --db --billing
```

Generates `UserService` microservice in `services/UserService/` with:

```
UserServiceApplication.java
UserServiceController.java
UserServiceBillingController.java ✅
pom.xml
src/main/resources/application.properties ✅
Dockerfile ✅
README.md ✅
```

---

## **Generated Service Structure**

```
services/UserService/
├── pom.xml
├── src/
│   └── main/
│       ├── java/
│       │   └── com/example/UserService/
│       │       ├── UserServiceApplication.java
│       │       ├── UserServiceController.java
│       │       └── UserServiceBillingController.java
│       └── resources/
│           └── application.properties
├── Dockerfile
└── README.md
```

---

## **Running Services**

### Locally

```bash
cd services/UserService
mvn package
java -jar target/UserService.jar
```

### Using Docker

```bash
docker build -t userservice .
docker run -p 8080:8080 userservice:latest
```

**Test endpoints:**

```bash
curl http://localhost:8080/api/userservice
curl -X POST http://localhost:8080/api/userservice/billing/subscribe/stripe
curl -X POST http://localhost:8080/api/userservice/billing/subscribe/paypal
```

---

## **How it works**

SpringRocket uses **Jinja2 templates** stored in `templates/`. When you run `create-service`, it:

1. Copies templates into a **Maven-compliant folder structure**
2. Replaces placeholders like `{{ServiceName}}`
3. Generates ready-to-run microservice boilerplate with optional Docker, DB, and billing

---

## **Next Steps**

* Extend BillingController with real Stripe or PayPal integration
* Add authentication, notifications, or other SaaS features
* Use SpringRocket as a base for small microservice teams or open-source projects

---

## **License**

MIT License — feel free to use, modify, and contribute.

---

If you want, I can **also add some visual flair** with:

* Badges (Python version, Docker build status)
* A tiny **demo GIF** showing `docker run` in action
* One-liner “wow” tagline for GitHub front page

Do you want me to do that next?
