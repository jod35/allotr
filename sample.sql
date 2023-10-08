CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(150) NOT NULL UNIQUE
) CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "codename" varchar(100) NOT NULL,
    "name" varchar(255) NOT NULL
) CREATE TABLE "courses_course" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "code" varchar(10) NOT NULL UNIQUE,
    "title" varchar(225) NOT NULL UNIQUE,
    "course_description" text NULL,
    "created_at" datetime NOT NULL
) CREATE TABLE "departments_department" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(500) NOT NULL,
    "department_head" varchar(255) NOT NULL,
    "contact_email" varchar(80) NOT NULL,
    "description" text NOT NULL,
    "created_at" datetime NOT NULL,
    "school_id" bigint NOT NULL REFERENCES "schools_school" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "object_id" text NULL,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0),
    "change_message" text NOT NULL,
    "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "action_time" datetime NOT NULL
) CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL
) CREATE TABLE "django_migrations" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app" varchar(255) NOT NULL,
    "name" varchar(255) NOT NULL,
    "applied" datetime NOT NULL
) CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
) CREATE TABLE "intakes_intake" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(50) NOT NULL,
    "start_date" datetime NULL,
    "end_date" date NULL,
    "academic_year" integer NOT NULL,
    "term" varchar(25) NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "is_active" bool NOT NULL
) CREATE TABLE "intakes_intakecourse" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "course_id" bigint NOT NULL REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED,
    "intake_id" bigint NOT NULL REFERENCES "intakes_intake" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "programs_program" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(255) NOT NULL,
    "code" varchar(10) NOT NULL,
    "years_of_study" integer NOT NULL,
    "degree_level" varchar(50) NOT NULL,
    "details" text NULL,
    "created_at" datetime NOT NULL,
    "department_id" bigint NOT NULL REFERENCES "departments_department" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "programs_programcourse" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "course_id" bigint NOT NULL REFERENCES "courses_course" ("id") DEFERRABLE INITIALLY DEFERRED,
    "program_id" bigint NOT NULL REFERENCES "programs_program" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "schools_school" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(255) NOT NULL UNIQUE,
    "dean" varchar(250) NOT NULL,
    "contact_email" varchar(80) NOT NULL,
    "details" text NOT NULL,
    "created_at" datetime NOT NULL,
    "updated" date NOT NULL,
    "code" varchar(5) NOT NULL UNIQUE
) CREATE TABLE sqlite_sequence(name, seq) CREATE TABLE "users_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NULL,
    "email" varchar(80) NOT NULL UNIQUE,
    "username" varchar(50) NOT NULL,
    "date_of_birth" date NULL,
    "date_joined" datetime NOT NULL,
    "first_name" varchar(150) NOT NULL,
    "is_active" bool NOT NULL,
    "is_staff" bool NOT NULL,
    "is_superuser" bool NOT NULL,
    "last_name" varchar(150) NOT NULL
) CREATE TABLE "users_user_groups" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE TABLE "users_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
) CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id") CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id") CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id") CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id") CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename") CREATE INDEX "departments_department_school_id_190979be" ON "departments_department" ("school_id") CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id") CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id") CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model") CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date") CREATE INDEX "intakes_intakecourse_course_id_5e752790" ON "intakes_intakecourse" ("course_id") CREATE INDEX "intakes_intakecourse_intake_id_45fbb0ac" ON "intakes_intakecourse" ("intake_id") CREATE INDEX "programs_program_department_id_a7847539" ON "programs_program" ("department_id") CREATE INDEX "programs_programcourse_course_id_b4c1d504" ON "programs_programcourse" ("course_id") CREATE INDEX "programs_programcourse_program_id_8dffe738" ON "programs_programcourse" ("program_id") CREATE INDEX "users_user_groups_group_id_9afc8d0e" ON "users_user_groups" ("group_id") CREATE INDEX "users_user_groups_user_id_5f6f5a90" ON "users_user_groups" ("user_id") CREATE UNIQUE INDEX "users_user_groups_user_id_group_id_b88eab82_uniq" ON "users_user_groups" ("user_id", "group_id") CREATE INDEX "users_user_user_permissions_permission_id_0b93982e" ON "users_user_user_permissions" ("permission_id") CREATE INDEX "users_user_user_permissions_user_id_20aca447" ON "users_user_user_permissions" ("user_id") CREATE UNIQUE INDEX "users_user_user_permissions_user_id_permission_id_43338c45_uniq" ON "users_user_user_permissions" ("user_id", "permission_id")

