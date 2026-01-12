# Django Authentication & Authorization System

Проект представляет собой **собственную систему аутентификации и авторизации**, реализованную на **Django** и **Django REST Framework (DRF)**. Система позволяет регистрировать пользователей, управлять их профилями и ограничивать доступ к ресурсам на основе ролей и разрешений.

---

## ✅ Особенности

- **Регистрация и аутентификация** пользователей по email и паролю.
- **JWT-токены** для аутентификации.
- **Собственная модель пользователя** (`User`).
- **Роли и разрешения** (RBAC-подобная система).
- **API для администратора** для управления ролями и правами.
- **Мягкое удаление** аккаунта.
- **Mock-объекты** для демонстрации бизнес-логики.

---

## 🧱 Архитектура системы

### Сущности

- `User` — пользователь системы.
- `Role` — роль (например, `admin`, `moderator`, `user`).
- `Permission` — разрешение (например, `project:read`, `project:write`).
- `RolePermission` — связь между ролью и разрешением.
- `UserAssignment` — связь между пользователем и ролью.

### Диаграмма связей

User ←→ UserAssignment → Role ←→ RolePermission → Permission

---

## 🧾 Примеры ролей и разрешений

| Роль        | Разрешения                         |
|-------------|------------------------------------|
| `admin`     | `*:*` (все действия)              |
| `moderator` | `project:read`, `comment:delete`  |
| `user`      | `project:read`                    |

---

## 🛠️ Используемые технологии

- **Django** — веб-фреймворк.
- **Django REST Framework** — API.
- **JWT** — аутентификация.
- **SQLite** — база данных (в проекте).
- **Python 3.8+**

---

## 📁 Структура проекта
```
django-auth-project/
├── manage.py
├── requirements.txt
├── README.md
├── config/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── auth_app/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
| ├── permissions.py
| ├── apps.py
│ └── migrations/
└── business_app/
├── views.py
├── models.py
└── urls.py
```
---

## 🚀 Запуск проекта

**1. Клонируйте репозиторий:**
```bash
git clone https://github.com/toxjc/django-auth-project.git
cd django-auth-project
```
**2. Установите зависимости:**
```bash
pip install -r requirements.txt
```
**3. Сделайте миграции:**
```bash
python manage.py makemigrations
python manage.py migrate
```
**4. Создайте суперпользователя:**
```bash
python manage.py createsuperuser
```
**5. Запустите сервер:**
```bash
python manage.py runserver
```
---

## 🧪 API Endpoints

**Пользовательские:**

| Метод  | Эндпоинт             | Описание                      |
|--------|----------------------|-------------------------------|
| POST   | `/auth/register/`    | Регистрация пользователя      |
| POST   | `/auth/login/`       | Вход в систему                |
| POST   | `/auth/logout/`      | Выход из системы              |
| PUT    | `/auth/profile/`     | Обновление профиля            |
| DELETE | `/auth/delete/`      | Мягкое удаление аккаунта      |

**Административные:**

| Метод  | Эндпоинт                          | Описание                         |
|--------|-----------------------------------|----------------------------------|
| GET    | `/auth/admin/roles/`              | Получить список ролей            |
| POST   | `/auth/admin/roles/`              | Создать роль                     |
| GET    | `/auth/admin/permissions/`        | Получить список разрешений       |
| POST   | `/auth/admin/permissions/`        | Создать разрешение               |
| POST   | `/auth/admin/assign-role/`        | Назначить роль пользователю      |
| POST   | `/auth/admin/assign-permission/`  | Назначить разрешение роли        |

---

## 📌 Статусы ошибок

**401 Unauthorized** — пользователь не аутентифицирован.

**403 Forbidden** — пользователь не имеет доступа.

**400 Bad Request** — неверные данные.