/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : new

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 14/04/2018 08:23:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (9, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (10, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (11, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add User Widget', 6, 'add_userwidget');
INSERT INTO `auth_permission` VALUES (22, 'Can change User Widget', 6, 'change_userwidget');
INSERT INTO `auth_permission` VALUES (23, 'Can delete User Widget', 6, 'delete_userwidget');
INSERT INTO `auth_permission` VALUES (24, 'Can add Bookmark', 7, 'add_bookmark');
INSERT INTO `auth_permission` VALUES (25, 'Can change Bookmark', 7, 'change_bookmark');
INSERT INTO `auth_permission` VALUES (26, 'Can delete Bookmark', 7, 'delete_bookmark');
INSERT INTO `auth_permission` VALUES (27, 'Can add User Setting', 8, 'add_usersettings');
INSERT INTO `auth_permission` VALUES (28, 'Can change User Setting', 8, 'change_usersettings');
INSERT INTO `auth_permission` VALUES (29, 'Can delete User Setting', 8, 'delete_usersettings');
INSERT INTO `auth_permission` VALUES (30, 'Can add log entry', 9, 'add_log');
INSERT INTO `auth_permission` VALUES (31, 'Can change log entry', 9, 'change_log');
INSERT INTO `auth_permission` VALUES (32, 'Can delete log entry', 9, 'delete_log');
INSERT INTO `auth_permission` VALUES (33, 'Can view Bookmark', 7, 'view_bookmark');
INSERT INTO `auth_permission` VALUES (34, 'Can view log entry', 9, 'view_log');
INSERT INTO `auth_permission` VALUES (35, 'Can view User Setting', 8, 'view_usersettings');
INSERT INTO `auth_permission` VALUES (36, 'Can view User Widget', 6, 'view_userwidget');
INSERT INTO `auth_permission` VALUES (37, 'Can add captcha store', 10, 'add_captchastore');
INSERT INTO `auth_permission` VALUES (38, 'Can change captcha store', 10, 'change_captchastore');
INSERT INTO `auth_permission` VALUES (39, 'Can delete captcha store', 10, 'delete_captchastore');
INSERT INTO `auth_permission` VALUES (40, 'Can view captcha store', 10, 'view_captchastore');
INSERT INTO `auth_permission` VALUES (41, 'Can add 房间', 11, 'add_room');
INSERT INTO `auth_permission` VALUES (42, 'Can change 房间', 11, 'change_room');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 房间', 11, 'delete_room');
INSERT INTO `auth_permission` VALUES (44, 'Can add 酒店', 12, 'add_hotel');
INSERT INTO `auth_permission` VALUES (45, 'Can change 酒店', 12, 'change_hotel');
INSERT INTO `auth_permission` VALUES (46, 'Can delete 酒店', 12, 'delete_hotel');
INSERT INTO `auth_permission` VALUES (47, 'Can add 轮播酒店', 12, 'add_bannerhotel');
INSERT INTO `auth_permission` VALUES (48, 'Can change 轮播酒店', 12, 'change_bannerhotel');
INSERT INTO `auth_permission` VALUES (49, 'Can delete 轮播酒店', 12, 'delete_bannerhotel');
INSERT INTO `auth_permission` VALUES (50, 'Can view 轮播酒店', 13, 'view_bannerhotel');
INSERT INTO `auth_permission` VALUES (51, 'Can view 酒店', 12, 'view_hotel');
INSERT INTO `auth_permission` VALUES (52, 'Can view 房间', 11, 'view_room');
INSERT INTO `auth_permission` VALUES (53, 'Can add 轮播图', 14, 'add_banner');
INSERT INTO `auth_permission` VALUES (54, 'Can change 轮播图', 14, 'change_banner');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 轮播图', 14, 'delete_banner');
INSERT INTO `auth_permission` VALUES (56, 'Can add 邮箱验证码', 15, 'add_emailverifyrecord');
INSERT INTO `auth_permission` VALUES (57, 'Can change 邮箱验证码', 15, 'change_emailverifyrecord');
INSERT INTO `auth_permission` VALUES (58, 'Can delete 邮箱验证码', 15, 'delete_emailverifyrecord');
INSERT INTO `auth_permission` VALUES (59, 'Can add 用户信息', 16, 'add_userprofile');
INSERT INTO `auth_permission` VALUES (60, 'Can change 用户信息', 16, 'change_userprofile');
INSERT INTO `auth_permission` VALUES (61, 'Can delete 用户信息', 16, 'delete_userprofile');
INSERT INTO `auth_permission` VALUES (62, 'Can view 轮播图', 14, 'view_banner');
INSERT INTO `auth_permission` VALUES (63, 'Can view 邮箱验证码', 15, 'view_emailverifyrecord');
INSERT INTO `auth_permission` VALUES (64, 'Can view 用户信息', 16, 'view_userprofile');
INSERT INTO `auth_permission` VALUES (65, 'Can add 城市', 17, 'add_citydict');
INSERT INTO `auth_permission` VALUES (66, 'Can change 城市', 17, 'change_citydict');
INSERT INTO `auth_permission` VALUES (67, 'Can delete 城市', 17, 'delete_citydict');
INSERT INTO `auth_permission` VALUES (68, 'Can add 门票', 18, 'add_ticket');
INSERT INTO `auth_permission` VALUES (69, 'Can change 门票', 18, 'change_ticket');
INSERT INTO `auth_permission` VALUES (70, 'Can delete 门票', 18, 'delete_ticket');
INSERT INTO `auth_permission` VALUES (71, 'Can add 景区信息', 19, 'add_spot');
INSERT INTO `auth_permission` VALUES (72, 'Can change 景区信息', 19, 'change_spot');
INSERT INTO `auth_permission` VALUES (73, 'Can delete 景区信息', 19, 'delete_spot');
INSERT INTO `auth_permission` VALUES (74, 'Can add 轮播景区', 19, 'add_bannerspot');
INSERT INTO `auth_permission` VALUES (75, 'Can change 轮播景区', 19, 'change_bannerspot');
INSERT INTO `auth_permission` VALUES (76, 'Can delete 轮播景区', 19, 'delete_bannerspot');
INSERT INTO `auth_permission` VALUES (77, 'Can view 轮播景区', 20, 'view_bannerspot');
INSERT INTO `auth_permission` VALUES (78, 'Can view 城市', 17, 'view_citydict');
INSERT INTO `auth_permission` VALUES (79, 'Can view 景区信息', 19, 'view_spot');
INSERT INTO `auth_permission` VALUES (80, 'Can view 门票', 18, 'view_ticket');
INSERT INTO `auth_permission` VALUES (81, 'Can add 行程', 21, 'add_schedule');
INSERT INTO `auth_permission` VALUES (82, 'Can change 行程', 21, 'change_schedule');
INSERT INTO `auth_permission` VALUES (83, 'Can delete 行程', 21, 'delete_schedule');
INSERT INTO `auth_permission` VALUES (84, 'Can add 轮播行程', 21, 'add_bannerschedule');
INSERT INTO `auth_permission` VALUES (85, 'Can change 轮播行程', 21, 'change_bannerschedule');
INSERT INTO `auth_permission` VALUES (86, 'Can delete 轮播行程', 21, 'delete_bannerschedule');
INSERT INTO `auth_permission` VALUES (87, 'Can view 轮播行程', 22, 'view_bannerschedule');
INSERT INTO `auth_permission` VALUES (88, 'Can view 行程', 21, 'view_schedule');
INSERT INTO `auth_permission` VALUES (89, 'Can add 用户消息', 23, 'add_usermessage');
INSERT INTO `auth_permission` VALUES (90, 'Can change 用户消息', 23, 'change_usermessage');
INSERT INTO `auth_permission` VALUES (91, 'Can delete 用户消息', 23, 'delete_usermessage');
INSERT INTO `auth_permission` VALUES (92, 'Can add 用户购买过的门票', 24, 'add_userspot');
INSERT INTO `auth_permission` VALUES (93, 'Can change 用户购买过的门票', 24, 'change_userspot');
INSERT INTO `auth_permission` VALUES (94, 'Can delete 用户购买过的门票', 24, 'delete_userspot');
INSERT INTO `auth_permission` VALUES (95, 'Can add 用户参观过的行程', 25, 'add_userschedule');
INSERT INTO `auth_permission` VALUES (96, 'Can change 用户参观过的行程', 25, 'change_userschedule');
INSERT INTO `auth_permission` VALUES (97, 'Can delete 用户参观过的行程', 25, 'delete_userschedule');
INSERT INTO `auth_permission` VALUES (98, 'Can add 用户预定过的酒店', 26, 'add_userhotel');
INSERT INTO `auth_permission` VALUES (99, 'Can change 用户预定过的酒店', 26, 'change_userhotel');
INSERT INTO `auth_permission` VALUES (100, 'Can delete 用户预定过的酒店', 26, 'delete_userhotel');
INSERT INTO `auth_permission` VALUES (101, 'Can add 用户购买', 27, 'add_userfavorite');
INSERT INTO `auth_permission` VALUES (102, 'Can change 用户购买', 27, 'change_userfavorite');
INSERT INTO `auth_permission` VALUES (103, 'Can delete 用户购买', 27, 'delete_userfavorite');
INSERT INTO `auth_permission` VALUES (104, 'Can view 用户购买', 27, 'view_userfavorite');
INSERT INTO `auth_permission` VALUES (105, 'Can view 用户预定过的酒店', 26, 'view_userhotel');
INSERT INTO `auth_permission` VALUES (106, 'Can view 用户消息', 23, 'view_usermessage');
INSERT INTO `auth_permission` VALUES (107, 'Can view 用户参观过的行程', 25, 'view_userschedule');
INSERT INTO `auth_permission` VALUES (108, 'Can view 用户购买过的门票', 24, 'view_userspot');
COMMIT;

-- ----------------------------
-- Table structure for captcha_captchastore
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (10, 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (13, 'hotels', 'bannerhotel');
INSERT INTO `django_content_type` VALUES (12, 'hotels', 'hotel');
INSERT INTO `django_content_type` VALUES (11, 'hotels', 'room');
INSERT INTO `django_content_type` VALUES (27, 'operation', 'userfavorite');
INSERT INTO `django_content_type` VALUES (26, 'operation', 'userhotel');
INSERT INTO `django_content_type` VALUES (23, 'operation', 'usermessage');
INSERT INTO `django_content_type` VALUES (25, 'operation', 'userschedule');
INSERT INTO `django_content_type` VALUES (24, 'operation', 'userspot');
INSERT INTO `django_content_type` VALUES (22, 'schedules', 'bannerschedule');
INSERT INTO `django_content_type` VALUES (21, 'schedules', 'schedule');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (20, 'spots', 'bannerspot');
INSERT INTO `django_content_type` VALUES (17, 'spots', 'citydict');
INSERT INTO `django_content_type` VALUES (19, 'spots', 'spot');
INSERT INTO `django_content_type` VALUES (18, 'spots', 'ticket');
INSERT INTO `django_content_type` VALUES (14, 'users', 'banner');
INSERT INTO `django_content_type` VALUES (15, 'users', 'emailverifyrecord');
INSERT INTO `django_content_type` VALUES (16, 'users', 'userprofile');
INSERT INTO `django_content_type` VALUES (7, 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES (9, 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES (8, 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES (6, 'xadmin', 'userwidget');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-04-14 05:19:55.980646');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2018-04-14 05:19:56.043155');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-04-14 05:19:56.164673');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2018-04-14 05:19:56.189730');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2018-04-14 05:19:56.199368');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2018-04-14 05:19:56.211152');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2018-04-14 05:19:56.222886');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2018-04-14 05:19:56.225630');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2018-04-14 05:19:56.236079');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2018-04-14 05:19:56.249620');
INSERT INTO `django_migrations` VALUES (11, 'users', '0001_initial', '2018-04-14 05:19:56.418039');
INSERT INTO `django_migrations` VALUES (12, 'admin', '0001_initial', '2018-04-14 05:19:56.489899');
INSERT INTO `django_migrations` VALUES (13, 'admin', '0002_logentry_remove_auto_add', '2018-04-14 05:19:56.522253');
INSERT INTO `django_migrations` VALUES (14, 'captcha', '0001_initial', '2018-04-14 05:19:56.541820');
INSERT INTO `django_migrations` VALUES (15, 'spots', '0001_initial', '2018-04-14 05:19:56.643064');
INSERT INTO `django_migrations` VALUES (16, 'hotels', '0001_initial', '2018-04-14 05:19:56.730765');
INSERT INTO `django_migrations` VALUES (17, 'schedules', '0001_initial', '2018-04-14 05:19:56.782842');
INSERT INTO `django_migrations` VALUES (18, 'operation', '0001_initial', '2018-04-14 05:19:56.886554');
INSERT INTO `django_migrations` VALUES (19, 'operation', '0002_auto_20180414_0516', '2018-04-14 05:19:57.238619');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2018-04-14 05:19:57.262735');
INSERT INTO `django_migrations` VALUES (21, 'xadmin', '0001_initial', '2018-04-14 05:19:57.509082');
INSERT INTO `django_migrations` VALUES (22, 'schedules', '0002_auto_20180414_0547', '2018-04-14 05:47:47.598073');
INSERT INTO `django_migrations` VALUES (23, 'schedules', '0003_schedule_price', '2018-04-14 06:01:23.821372');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('llr9diamid77vdwogrbmentt8l5cret1', 'ZWM3OGMwYTBmMDk2MzM5NmM4NzA5YjU0Y2I2MmY1MTg3NjE5MmU1NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjhmNjJmMjhlMTA1YTZhMGQ5MzNiZjUyN2IxNTJkYTMzNzM2Mjg1NjciLCJMSVNUX1FVRVJZIjpbWyJvcGVyYXRpb24iLCJ1c2Vyc2NoZWR1bGUiXSwiIl19', '2018-04-28 06:02:46.116576');
INSERT INTO `django_session` VALUES ('wgbjr7m25p5hlkalo98pxrqihgv9ki00', 'OWIyZDljZDg5MzMxZTFkNTdiYmQxNTkyM2E3NzExYjBiOTMyMjFjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjhmNjJmMjhlMTA1YTZhMGQ5MzNiZjUyN2IxNTJkYTMzNzM2Mjg1NjciLCJuYXZfbWVudSI6Ilt7XCJ0aXRsZVwiOiBcIlx1NjY2Zlx1NTMzYVx1N2JhMVx1NzQwNlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NTdjZVx1NWUwMlwiLCBcInVybFwiOiBcIi9hZG1pbi9zcG90cy9jaXR5ZGljdC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTJ9LCB7XCJ0aXRsZVwiOiBcIlx1NjY2Zlx1NTMzYVx1NGZlMVx1NjA2ZlwiLCBcInVybFwiOiBcIi9hZG1pbi9zcG90cy9zcG90L1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxM30sIHtcInRpdGxlXCI6IFwiXHU5NWU4XHU3OTY4XCIsIFwidXJsXCI6IFwiL2FkbWluL3Nwb3RzL3RpY2tldC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTR9XSwgXCJmaXJzdF91cmxcIjogXCIvYWRtaW4vc3BvdHMvY2l0eWRpY3QvXCJ9LCB7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1NGZlMVx1NjA2ZlwiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1NGZlMVx1NjA2ZlwiLCBcInVybFwiOiBcIi9hZG1pbi91c2Vycy91c2VycHJvZmlsZS9cIiwgXCJpY29uXCI6IFwiZmEgZmEtdXNlclwiLCBcIm9yZGVyXCI6IDN9LCB7XCJ0aXRsZVwiOiBcIlx1OTBhZVx1N2JiMVx1OWE4Y1x1OGJjMVx1NzgwMVwiLCBcInVybFwiOiBcIi9hZG1pbi91c2Vycy9lbWFpbHZlcmlmeXJlY29yZC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTB9LCB7XCJ0aXRsZVwiOiBcIlx1OGY2ZVx1NjRhZFx1NTZmZVwiLCBcInVybFwiOiBcIi9hZG1pbi91c2Vycy9iYW5uZXIvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDExfV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLXVzZXJcIiwgXCJmaXJzdF91cmxcIjogXCIvYWRtaW4vdXNlcnMvdXNlcnByb2ZpbGUvXCJ9LCB7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1NjRjZFx1NGY1Y1wiLCBcIm1lbnVzXCI6IFt7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1OGQyZFx1NGU3MFwiLCBcInVybFwiOiBcIi9hZG1pbi9vcGVyYXRpb24vdXNlcmZhdm9yaXRlL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxN30sIHtcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU2ZDg4XHU2MDZmXCIsIFwidXJsXCI6IFwiL2FkbWluL29wZXJhdGlvbi91c2VybWVzc2FnZS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTh9LCB7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1NTNjMlx1ODljMlx1OGZjN1x1NzY4NFx1ODg0Y1x1N2EwYlwiLCBcInVybFwiOiBcIi9hZG1pbi9vcGVyYXRpb24vdXNlcnNjaGVkdWxlL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAxOX0sIHtcInRpdGxlXCI6IFwiXHU3NTI4XHU2MjM3XHU4ZDJkXHU0ZTcwXHU4ZmM3XHU3Njg0XHU5NWU4XHU3OTY4XCIsIFwidXJsXCI6IFwiL2FkbWluL29wZXJhdGlvbi91c2Vyc3BvdC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMjB9LCB7XCJ0aXRsZVwiOiBcIlx1NzUyOFx1NjIzN1x1OTg4NFx1NWI5YVx1OGZjN1x1NzY4NFx1OTE1Mlx1NWU5N1wiLCBcInVybFwiOiBcIi9hZG1pbi9vcGVyYXRpb24vdXNlcmhvdGVsL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiAyMX1dLCBcImZpcnN0X3VybFwiOiBcIi9hZG1pbi9vcGVyYXRpb24vdXNlcmZhdm9yaXRlL1wifSwge1widGl0bGVcIjogXCJcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTY1ZTVcdTVmZDdcdThiYjBcdTVmNTVcIiwgXCJ1cmxcIjogXCIvYWRtaW4veGFkbWluL2xvZy9cIiwgXCJpY29uXCI6IFwiZmEgZmEtY29nXCIsIFwib3JkZXJcIjogNn1dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS1jb2dcIiwgXCJmaXJzdF91cmxcIjogXCIvYWRtaW4veGFkbWluL2xvZy9cIn0sIHtcInRpdGxlXCI6IFwiXHU4ODRjXHU3YTBiXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU4ODRjXHU3YTBiXCIsIFwidXJsXCI6IFwiL2FkbWluL3NjaGVkdWxlcy9zY2hlZHVsZS9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogMTV9LCB7XCJ0aXRsZVwiOiBcIlx1OGY2ZVx1NjRhZFx1ODg0Y1x1N2EwYlwiLCBcInVybFwiOiBcIi9hZG1pbi9zY2hlZHVsZXMvYmFubmVyc2NoZWR1bGUvXCIsIFwiaWNvblwiOiBudWxsLCBcIm9yZGVyXCI6IDE2fV0sIFwiZmlyc3RfdXJsXCI6IFwiL2FkbWluL3NjaGVkdWxlcy9zY2hlZHVsZS9cIn0sIHtcInRpdGxlXCI6IFwiXHU4YmE0XHU4YmMxXHU1NDhjXHU2Mzg4XHU2NzQzXCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU3ZWM0XCIsIFwidXJsXCI6IFwiL2FkbWluL2F1dGgvZ3JvdXAvXCIsIFwiaWNvblwiOiBcImZhIGZhLWdyb3VwXCIsIFwib3JkZXJcIjogMn0sIHtcInRpdGxlXCI6IFwiXHU2NzQzXHU5NjUwXCIsIFwidXJsXCI6IFwiL2FkbWluL2F1dGgvcGVybWlzc2lvbi9cIiwgXCJpY29uXCI6IFwiZmEgZmEtbG9ja1wiLCBcIm9yZGVyXCI6IDR9XSwgXCJmaXJzdF9pY29uXCI6IFwiZmEgZmEtZ3JvdXBcIiwgXCJmaXJzdF91cmxcIjogXCIvYWRtaW4vYXV0aC9ncm91cC9cIn0sIHtcInRpdGxlXCI6IFwiXHU5MTUyXHU1ZTk3XHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU5MTUyXHU1ZTk3XCIsIFwidXJsXCI6IFwiL2FkbWluL2hvdGVscy9ob3RlbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogN30sIHtcInRpdGxlXCI6IFwiXHU4ZjZlXHU2NGFkXHU5MTUyXHU1ZTk3XCIsIFwidXJsXCI6IFwiL2FkbWluL2hvdGVscy9iYW5uZXJob3RlbC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogOH0sIHtcInRpdGxlXCI6IFwiXHU2MjNmXHU5NWY0XCIsIFwidXJsXCI6IFwiL2FkbWluL2hvdGVscy9yb29tL1wiLCBcImljb25cIjogbnVsbCwgXCJvcmRlclwiOiA5fV0sIFwiZmlyc3RfdXJsXCI6IFwiL2FkbWluL2hvdGVscy9ob3RlbC9cIn1dIiwiTElTVF9RVUVSWSI6W1siaG90ZWxzIiwiaG90ZWwiXSwiIl19', '2018-04-28 07:54:07.665220');
COMMIT;

-- ----------------------------
-- Table structure for hotels_hotel
-- ----------------------------
DROP TABLE IF EXISTS `hotels_hotel`;
CREATE TABLE `hotels_hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(150) NOT NULL,
  `name` varchar(52) NOT NULL,
  `desc` varchar(300) NOT NULL,
  `detail` longtext NOT NULL,
  `category` varchar(2) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `is_banner` tinyint(1) NOT NULL,
  `tag` varchar(10) NOT NULL,
  `youneed_konw` varchar(300) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hotels_hotel_city_id_68c70157_fk_spots_citydict_id` (`city_id`),
  CONSTRAINT `hotels_hotel_city_id_68c70157_fk_spots_citydict_id` FOREIGN KEY (`city_id`) REFERENCES `spots_citydict` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hotels_hotel
-- ----------------------------
BEGIN;
INSERT INTO `hotels_hotel` VALUES (1, '测试', '测试', '测试', '<p><img src=\"/media/3_20180414075330_347.jpg\" title=\"\" alt=\"3.jpg\"/><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=116.404,39.915&zoom=10&width=530&height=340&markers=116.404,39.915\"/></p>', '1', 5, 'hotel/2018/04/4_cZhMdUL.jpg', 0, 0, '热门销售', '测试信息', '2018-04-14 05:44:00.000000', 2);
COMMIT;

-- ----------------------------
-- Table structure for hotels_room
-- ----------------------------
DROP TABLE IF EXISTS `hotels_room`;
CREATE TABLE `hotels_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(300) NOT NULL,
  `price` int(11) NOT NULL,
  `detail` longtext NOT NULL,
  `degree` varchar(2) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hotels_room_hotel_id_0ee74c95_fk_hotels_hotel_id` (`hotel_id`),
  CONSTRAINT `hotels_room_hotel_id_0ee74c95_fk_hotels_hotel_id` FOREIGN KEY (`hotel_id`) REFERENCES `hotels_hotel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hotels_room
-- ----------------------------
BEGIN;
INSERT INTO `hotels_room` VALUES (1, '测试', '测试', 2320, '测试测试测试测试', '1', 0, 'hotelroom/2018/04/3.jpg', 14, '2018-04-14 05:44:00.000000', 1);
COMMIT;

-- ----------------------------
-- Table structure for operation_userfavorite
-- ----------------------------
DROP TABLE IF EXISTS `operation_userfavorite`;
CREATE TABLE `operation_userfavorite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fav_id` int(11) NOT NULL,
  `fav_type` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_userfavorite_user_id_ad46a6af_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_userfavorite_user_id_ad46a6af_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_userfavorite
-- ----------------------------
BEGIN;
INSERT INTO `operation_userfavorite` VALUES (1, 1, 3, '2018-04-14 05:43:43.157269', 1);
INSERT INTO `operation_userfavorite` VALUES (2, 1, 2, '2018-04-14 05:45:18.712436', 1);
INSERT INTO `operation_userfavorite` VALUES (3, 1, 2, '2018-04-14 06:13:34.727049', 1);
INSERT INTO `operation_userfavorite` VALUES (4, 7, 3, '2018-04-14 06:15:51.281811', 1);
INSERT INTO `operation_userfavorite` VALUES (5, 2, 1, '2018-04-14 06:35:57.849528', 1);
INSERT INTO `operation_userfavorite` VALUES (6, 2, 1, '2018-04-14 06:36:04.216711', 1);
INSERT INTO `operation_userfavorite` VALUES (7, 2, 1, '2018-04-14 06:36:54.048915', 1);
INSERT INTO `operation_userfavorite` VALUES (8, 1, 2, '2018-04-14 06:38:20.508280', 1);
INSERT INTO `operation_userfavorite` VALUES (9, 2, 1, '2018-04-14 06:38:25.937101', 1);
INSERT INTO `operation_userfavorite` VALUES (10, 1, 2, '2018-04-14 07:07:46.419864', 1);
INSERT INTO `operation_userfavorite` VALUES (11, 7, 3, '2018-04-14 07:26:47.763672', 1);
INSERT INTO `operation_userfavorite` VALUES (12, 6, 3, '2018-04-14 07:37:59.378978', 1);
INSERT INTO `operation_userfavorite` VALUES (13, 1, 2, '2018-04-14 07:43:43.729208', 1);
INSERT INTO `operation_userfavorite` VALUES (14, 2, 1, '2018-04-14 07:57:00.530557', 1);
INSERT INTO `operation_userfavorite` VALUES (15, 2, 1, '2018-04-14 07:57:18.538639', 1);
INSERT INTO `operation_userfavorite` VALUES (16, 2, 1, '2018-04-14 07:57:22.397410', 1);
COMMIT;

-- ----------------------------
-- Table structure for operation_userhotel
-- ----------------------------
DROP TABLE IF EXISTS `operation_userhotel`;
CREATE TABLE `operation_userhotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_userhotel_hotel_id_676daddd_fk_hotels_room_id` (`hotel_id`),
  KEY `operation_userhotel_user_id_bc282e42_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_userhotel_hotel_id_676daddd_fk_hotels_room_id` FOREIGN KEY (`hotel_id`) REFERENCES `hotels_room` (`id`),
  CONSTRAINT `operation_userhotel_user_id_bc282e42_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_userhotel
-- ----------------------------
BEGIN;
INSERT INTO `operation_userhotel` VALUES (1, '2018-04-14 05:45:18.726914', 1, 1);
INSERT INTO `operation_userhotel` VALUES (2, '2018-04-14 06:13:34.743003', 1, 1);
INSERT INTO `operation_userhotel` VALUES (3, '2018-04-14 06:38:20.523323', 1, 1);
INSERT INTO `operation_userhotel` VALUES (4, '2018-04-14 07:07:46.431686', 1, 1);
INSERT INTO `operation_userhotel` VALUES (5, '2018-04-14 07:43:43.741983', 1, 1);
COMMIT;

-- ----------------------------
-- Table structure for operation_usermessage
-- ----------------------------
DROP TABLE IF EXISTS `operation_usermessage`;
CREATE TABLE `operation_usermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `has_read` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_usermessage
-- ----------------------------
BEGIN;
INSERT INTO `operation_usermessage` VALUES (1, 1, '恭喜您购买 哈尔滨冰雪大世界门票 门票成功，祝你出行愉快', 1, '2018-04-14 05:43:43.193993');
INSERT INTO `operation_usermessage` VALUES (2, 1, '恭喜您预定 测试 酒店成功，祝你出行愉快', 1, '2018-04-14 05:45:18.736809');
INSERT INTO `operation_usermessage` VALUES (3, 1, '恭喜您预定 测试 酒店成功，祝你出行愉快', 1, '2018-04-14 06:13:34.752867');
INSERT INTO `operation_usermessage` VALUES (4, 1, '恭喜您购买 东方明珠 门票成功，祝你出行愉快', 1, '2018-04-14 06:15:51.301466');
INSERT INTO `operation_usermessage` VALUES (5, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 06:35:57.865618');
INSERT INTO `operation_usermessage` VALUES (6, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 06:36:04.228624');
INSERT INTO `operation_usermessage` VALUES (7, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 06:36:54.082652');
INSERT INTO `operation_usermessage` VALUES (8, 1, '恭喜您预定 测试 酒店成功，祝你出行愉快', 1, '2018-04-14 06:38:20.542263');
INSERT INTO `operation_usermessage` VALUES (9, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 06:38:25.979669');
INSERT INTO `operation_usermessage` VALUES (10, 1, '恭喜您预定 测试 酒店成功，祝你出行愉快', 1, '2018-04-14 07:07:46.441258');
INSERT INTO `operation_usermessage` VALUES (11, 1, '恭喜您购买 东方明珠 门票成功，祝你出行愉快', 1, '2018-04-14 07:26:47.782156');
INSERT INTO `operation_usermessage` VALUES (12, 1, '恭喜您购买 布达拉宫门票 门票成功，祝你出行愉快', 1, '2018-04-14 07:37:00.000000');
INSERT INTO `operation_usermessage` VALUES (13, 1, '恭喜您预定 测试 酒店成功，祝你出行愉快', 1, '2018-04-14 07:43:43.749218');
INSERT INTO `operation_usermessage` VALUES (14, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 07:57:00.562832');
INSERT INTO `operation_usermessage` VALUES (15, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 07:57:18.574207');
INSERT INTO `operation_usermessage` VALUES (16, 1, '恭喜您购买 测试111 行程成功，祝你出行愉快', 1, '2018-04-14 07:57:22.431252');
COMMIT;

-- ----------------------------
-- Table structure for operation_userschedule
-- ----------------------------
DROP TABLE IF EXISTS `operation_userschedule`;
CREATE TABLE `operation_userschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `schedule_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_usersche_schedule_id_a84699a6_fk_schedules_schedule_id` (`schedule_id`),
  KEY `operation_userschedule_user_id_2befe116_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_usersche_schedule_id_a84699a6_fk_schedules_schedule_id` FOREIGN KEY (`schedule_id`) REFERENCES `schedules_schedule` (`id`),
  CONSTRAINT `operation_userschedule_user_id_2befe116_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_userschedule
-- ----------------------------
BEGIN;
INSERT INTO `operation_userschedule` VALUES (1, '2018-04-14 06:35:57.859273', 2, 1);
INSERT INTO `operation_userschedule` VALUES (2, '2018-04-14 06:36:04.225202', 2, 1);
INSERT INTO `operation_userschedule` VALUES (3, '2018-04-14 06:36:54.064955', 2, 1);
INSERT INTO `operation_userschedule` VALUES (4, '2018-04-14 06:38:25.960657', 2, 1);
INSERT INTO `operation_userschedule` VALUES (5, '2018-04-14 07:57:00.556939', 2, 1);
INSERT INTO `operation_userschedule` VALUES (6, '2018-04-14 07:57:18.561990', 2, 1);
INSERT INTO `operation_userschedule` VALUES (7, '2018-04-14 07:57:22.420218', 2, 1);
COMMIT;

-- ----------------------------
-- Table structure for operation_userspot
-- ----------------------------
DROP TABLE IF EXISTS `operation_userspot`;
CREATE TABLE `operation_userspot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `spot_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_userspot_spot_id_3eca6b5e_fk_spots_ticket_id` (`spot_id`),
  KEY `operation_userspot_user_id_bb6387cf_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_userspot_spot_id_3eca6b5e_fk_spots_ticket_id` FOREIGN KEY (`spot_id`) REFERENCES `spots_ticket` (`id`),
  CONSTRAINT `operation_userspot_user_id_bb6387cf_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_userspot
-- ----------------------------
BEGIN;
INSERT INTO `operation_userspot` VALUES (1, '2018-04-14 05:43:43.175787', 1, 1);
INSERT INTO `operation_userspot` VALUES (2, '2018-04-14 06:15:51.292590', 7, 1);
INSERT INTO `operation_userspot` VALUES (3, '2018-04-14 07:26:47.775496', 7, 1);
INSERT INTO `operation_userspot` VALUES (4, '2018-04-14 07:37:59.396309', 6, 1);
COMMIT;

-- ----------------------------
-- Table structure for schedules_schedule
-- ----------------------------
DROP TABLE IF EXISTS `schedules_schedule`;
CREATE TABLE `schedules_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(52) NOT NULL,
  `desc` varchar(300) NOT NULL,
  `detail` longtext NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `is_banner` tinyint(1) NOT NULL,
  `category` varchar(2) NOT NULL,
  `tag` varchar(10) NOT NULL,
  `youneed_konw` varchar(300) NOT NULL,
  `address` varchar(150) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `city_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `schedules_schedule_city_id_30a2869e_fk_spots_citydict_id` (`city_id`),
  CONSTRAINT `schedules_schedule_city_id_30a2869e_fk_spots_citydict_id` FOREIGN KEY (`city_id`) REFERENCES `spots_citydict` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of schedules_schedule
-- ----------------------------
BEGIN;
INSERT INTO `schedules_schedule` VALUES (1, '测试', '测试', '', 0, 'schedule/2018/04/3_b9PzUj8.jpg', 32, 1, '1', '行程备注', '测试信息', '测试', '2018-04-14 05:46:00.000000', 1, 0);
INSERT INTO `schedules_schedule` VALUES (2, '测试111', '测试111', '', 7, 'schedule/2018/04/1_HsbNIRD.jpg', 40, 0, '2', '行程备注', '测试111', '测试111', '2018-04-14 05:52:00.000000', 1, 200);
COMMIT;

-- ----------------------------
-- Table structure for spots_citydict
-- ----------------------------
DROP TABLE IF EXISTS `spots_citydict`;
CREATE TABLE `spots_citydict` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `desc` longtext NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spots_citydict
-- ----------------------------
BEGIN;
INSERT INTO `spots_citydict` VALUES (1, '黑龙江省黑河市', '黑河市地处中国东北边陲，黑龙江省西北部，小兴安岭北麓，位于北纬47°42′-51°03′，东经124°45′-129°18′之间，素有“中俄之窗”、“欧亚之门”等美誉。市区以黑龙江主航道中心为界，与俄罗斯远东地区第三大城市、阿穆尔州首府——布拉戈维申斯克市隔江相望，最近距离仅750米，是中俄4374公里边境线上，唯一一个与俄联邦主体首府相对应的距离最近、规模最大、规格最高、功能最全、开放最早的边境城市。黑河地区总面积68726平方千米，市辖区面积约14446平方千米，人口173万。黑河市是中国首批沿边开放城市，是黑龙江省重要的对俄贸易城市，是一座幅员辽阔、区位优越、资源富集、环境优美的旅游城市。', '2018-04-13 18:37:00.000000');
INSERT INTO `spots_citydict` VALUES (2, '黑龙江省北安市', '位于松嫩平原东北部滨北、齐北、北黑3条铁路交汇处。1945年建立人民政权，曾是黑龙江省省会。土地资源丰富，有多座国营农场。盛产小麦、大豆和马铃薯，是重要的农产品集散中心。东部森林资源丰富。工业以食品、机、木材、电力为主。交通便利,有绥北、齐北、黑北3条铁路交汇于此，是进出中国北方重要边贸城市黑河及旅游胜地五大连池的交通枢纽。', '2018-04-13 18:40:00.000000');
INSERT INTO `spots_citydict` VALUES (3, '黑龙江省哈尔滨', '哈尔滨，黑龙江省省会、副省级市、特大城市、中国东北地区中心城市之一，是东北北部交通、政治、经济、文化、金融中心，也是中国省辖市中陆地管辖面积最大、户籍人口居第三位的特大城市，地处中国东北平原东北部地区、黑龙江省南部，国家重要的制造业基地。哈尔滨地处东北亚中心地带，被誉为欧亚大陆桥的明珠，是第一条欧亚大陆桥和空中走廊的重要枢纽，也是中国历史文化名城、热点旅游城市和国际冰雪文化名城。是国家战略定位的“沿边开发开放中心城市”、“东北亚区域中心城市”及“对俄合作中心城市”。', '2018-04-13 18:42:00.000000');
INSERT INTO `spots_citydict` VALUES (4, '长沙', '长沙市隶属湖南省，湖南省省会，简称长，地处湖南省东部偏北，湘江下游和湘浏盆地西缘，是全国两型社会建设综合配套改革试验区核心城市，国家十二五规划确定的重点开发区域，湖南省的政治、经济、文化、科教和商贸中心。长沙是楚文明和湘楚文化的发源地，有3000年悠久的历史文化，约有2400年建城史，在春秋战国时期始建城，属楚国。因屈原和贾谊的影响而被称为“屈贾之乡”。长沙又称“楚汉名城”，马王堆汉墓和走马楼简牍等重要文物的出土反映其深厚的楚文化以及湖湘文化底蕴，位于岳麓山下的岳麓书院为湖南文化教育的象征。历史上涌现众多名人，留下众多的历史文化遗迹，成为首批国家历史文化名城。', '2018-04-13 18:43:00.000000');
INSERT INTO `spots_citydict` VALUES (5, '成都', '成都（Chengdu），简称蓉，四川省会，1993年被国务院确定为西南地区的科技、商贸、金融中心和交通、通讯枢纽，是设立外国领事馆数量最多、开通国际航线数量最多的中西部城市 。2015年由国务院批复并升格为国家重要的高新技术产业基地、商贸物流中心和综合交通枢纽，西部地区重要的中心城市 。成都位于位于四川盆地西部，成都平原腹地，成都东与德阳、资阳毗邻，西与雅安、阿坝接壤，南与眉山相连。成都是“首批国家历史文化名城”和“中国最佳旅游城市”，承载着三千余年的历史，拥有都江堰、武侯祠、杜甫草堂、金沙遗址、明蜀王陵、望江楼、青羊宫等众多名胜古迹和人文景观。联合国世界旅游组织第22届全体大会将于2017年、第22届世界航线发展大会将于2016年在成都举办。', '2018-04-13 18:47:00.000000');
INSERT INTO `spots_citydict` VALUES (6, '重庆', '重庆，简称巴和渝，别称巴渝、山城、渝都、桥都，雾都，是中华人民共和国中央直辖市、国家中心城市、超大城市、世界温泉之都、长江上游地区经济中心、金融中心和创新中心，政治、文化、科技、教育、艺术等中心，国务院定位的国际大都市。中西部水、陆、空型综合交通枢纽。 \r\n重庆因嘉陵江古称“渝水”，故重庆简称“渝”。北宋崇宁元年（1102年），改渝州为恭州。南宋淳熙16年（1189年）正月，孝宗之子赵惇先封恭王，二月即帝位为宋光宗皇帝，称为“双重喜庆”，遂升恭州为重庆府，重庆由此而得名。 \r\n抗日战争时期，中华民国政府定重庆为战时首都和永久陪都，共和国成立初期为西南大区驻地和中央直辖市，1997年6月18日恢复成立中央直辖市后，重庆老工业基地改造振兴步伐加快，形成了电子信息、汽车、装备制造、综合化工、材料、能源和消费品制造等千亿级产业集群，农业农村和金融、商贸物流、服务外包等现代服务业快速发展。 \r\n重庆拥有中新（重庆）战略性互联互通示范项目、国家级新区——两江新区、渝新欧国际铁路、重庆两路寸滩保税港区、重庆西永综合保税区、重庆铁路保税物流中心、重庆南彭公路保税物流中心、万州保税物流中心、过境72小时内免签，进口整车、水果、肉类等口岸。', '2018-04-13 18:49:00.000000');
INSERT INTO `spots_citydict` VALUES (7, '昆明', '昆明，享“春城”之美誉，云南省会，中国面向东南亚、南亚开放的门户城市，国家级历史文化名城，我国重要的旅游、商贸城市，西部地区重要的中心城市之一。 \r\n昆明地处云贵高原中部，是滇中城市群的核心圈、亚洲5小时航空圈的中心，国家一级物流园区布局城市之一。昆明市为山原地貌。地势大致北高南低，多溶洞和溶岩地貌，溶岩盆地有石林坝子。属北亚热带低纬高原山地季风气候。年平均气温16.5℃，年均降雨量1450毫米，无霜期278天，气候宜人。 \r\n昆明市是灵秀而迷人的，它三面环山，南濒滇池，湖光山色，天然成趣。滇池是云南省最大的高原湖泊，全国第六大淡水湖泊，沿湖两岸风光绮丽。由于地处低纬高原而形成“四季如春”的气候，特别是有高原湖泊滇池在调节着温湿度，使这里空气清新、天高云淡、阳光明媚、鲜花常开。 \r\n昆明市开放而时尚，浓缩了云南的区位优势，从两千多年前的“南方丝绸之路”到开放的昆明一直是东亚大陆与中南半岛、南亚次大陆各国进行经济贸易往来及政治联系的陆路枢纽。“中国昆明出口商品交易会”、“中国国际旅游交易会”、“中国昆明国际旅游节”使昆明成为中国主要的会展城市之一。2017世界春城60佳排行榜排名第三。', '2018-04-13 18:50:00.000000');
INSERT INTO `spots_citydict` VALUES (8, '丽江', '丽江市，云南省辖地级市，位于云南省西北部云贵高原与青藏高原的连接部位，市区中心位于东经100°25\'北纬26°86\'，海拔高度为2418米。北连迪庆藏族自治州，南接大理白族自治州，西邻怒江傈僳族自治州，东与四川凉山彝族自治州和攀枝花市接壤。丽江古城区是中国罕见的保存相当完好的少数民族古城，集中了纳西文化的精华，完整地保留了宋、元以来形成的历史风貌。 丽江自古以来是丝绸之路和茶马古道的中转站，丽江有建于南宋的丽江古城，纳西族名称叫“巩本知”，“巩本”为仓廪，“知”即集市，丽江古城曾是仓廪集散之地。', '2018-04-13 18:51:00.000000');
INSERT INTO `spots_citydict` VALUES (9, '西藏', '西藏自治区，古称“蕃”，简称“藏”，首府拉萨，是中国五个少数民族自治区之一。西藏以其雄伟壮观、神奇瑰丽的自然风光闻名。它地域辽阔，地貌壮观、资源丰富。自古以来，这片土地上的人们创造了丰富灿烂的民族文化。', '2018-04-13 18:52:00.000000');
INSERT INTO `spots_citydict` VALUES (10, '北京', '北京（Beijing），简称京，中华人民共和国首都、直辖市、国家中心城市、超大城市，全国政治中心、文化中心、国际交往中心、科技创新中心，是中国共产党中央委员会、中华人民共和国中央人民政府和全国人民代表大会的办公所在地。\r\n北京位于东经115.7°—117.4°，北纬39.4°—41.6°，中心位于北纬39°54′20″，东经116°25′29″，总面积16410.54平方千米。北京位于华北平原北部，背靠燕山，毗邻天津市和河北省。北京的气候为典型的北温带半湿润大陆性季风气候。\r\n北京历史悠久，文化灿烂，是首批国家历史文化名城、中国四大古都之一和世界上拥有世界文化遗产数最多的城市，3060年的建城史孕育了故宫、天坛、八达岭长城、颐和园等众多名胜古迹。早在七十万年前，北京周口店地区就出现了原始人群部落“北京人”。公元前1045年，北京成为蓟、燕等诸侯国的都城。公元938年以来，北京先后成为辽陪都、金中都、元大都、明清国都。1949年10月1日成为中华人民共和国首都。\r\n2015年末，北京全市常住人口2170.5万人，比2014年末增加18.9万人。其中，常住外来人口822.6万人，占常住人口的比重为37.9%。2015年北京市实现地区生产总值22968.6亿元，比2014年增长6.9%。\r\n2015年7月31日，国际奥委会主席巴赫宣布北京携手张家口获得2022年冬季奥林匹克运动会的举办权。北京由此成为全球首个既举办过夏季奥运会又即将举办冬季奥运会的城市。', '2018-04-13 18:53:00.000000');
INSERT INTO `spots_citydict` VALUES (11, '上海', '上海，简称“沪”或“申”，是中国共产党的诞生地。中华人民共和国直辖市，国家中心城市，超大城市，中国的经济、交通、科技、工业、金融、贸易、会展和航运中心，首批沿海开放城市。上海地处长江入海口，是长江经济带的龙头城市，隔东中国海与日本九州岛相望，南濒杭州湾，北、西与江苏、浙江两省相接。\r\n上海是一座国家历史文化名城，拥有深厚的近代城市文化底蕴和众多历史古迹。江南传统吴越文化与西方传入的工业文化相融合形成上海特有的海派文化， 上海人多属江浙民系使用吴语。早在宋代就有了“上海”之名，1843年后上海成为对外开放的商埠并迅速发展成为远东第一大城市，今日的上海已经成功举办了2010年世界博览会、中国上海国际艺术节、上海国际电影节等大型国际活动。\r\n上海辖16个市辖区，总面积6340平方公里，属亚热带湿润季风气候，四季分明，日照充分，雨量充沛。上海气候温和湿润，春秋较短，冬暖夏凉。1月份最冷，平均气温约4℃，通常7月份最热，平均气温约28℃。\r\n上海是中国重要的的经济、交通、科技、工业、金融、会展和航运中心，是世界上规模和面积最大的都会区之一。上海港货物吞吐量和集装箱吞吐量均居世界第一，是一个良好的滨江滨海国际性港口。上海也是中国大陆首个自贸区“中国（上海）自由贸易试验区”所在地。上海与江苏、浙江、安徽共同构成的长江三角洲城市群已成为国际6大世界级城市群之一。', '2018-04-13 20:47:00.000000');
COMMIT;

-- ----------------------------
-- Table structure for spots_spot
-- ----------------------------
DROP TABLE IF EXISTS `spots_spot`;
CREATE TABLE `spots_spot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `category` varchar(20) NOT NULL,
  `desc` longtext NOT NULL,
  `detail` longtext NOT NULL,
  `tag` varchar(10) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `visit_nums` int(11) NOT NULL,
  `is_banner` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(150) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `spots_spot_city_id_49d4c225_fk_spots_citydict_id` (`city_id`),
  CONSTRAINT `spots_spot_city_id_49d4c225_fk_spots_citydict_id` FOREIGN KEY (`city_id`) REFERENCES `spots_citydict` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spots_spot
-- ----------------------------
BEGIN;
INSERT INTO `spots_spot` VALUES (1, '大岛贸易区', '1', '黑河大岛处于黑龙江主航道中方一侧，位于黑河市与俄布拉戈维申斯克市之间，距俄布市仅750米，与黑河市区有大黑河岛桥相连，面积0.97平方公里。历经七年多的开发建设，岛上已建成民贸市场、洽谈中心、不夜城商服一条街、国际展厅等设施，是集旅游、贸易、娱乐等多功能于一体的旅贸娱乐岛。黑龙江省人民政府于1997年3月正式批准在大黑河岛设立边民互市贸易区，为黑河市民间互市贸易的发展提供了有利的条件和难得的机遇。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=127.523896,50.255988&zoom=14&width=530&height=340&markers=127.523896,50.255988\"/> </p><p><br/> </p>', '全国知名', 1, 80001, 20, 0, 'spot/2018/04/t01eab8cd2f083a6a0e.jpg', '黑龙江省黑河市', '2018-04-14 05:23:11.000000', 1);
INSERT INTO `spots_spot` VALUES (2, '冰雪大世界', '2', '中国哈尔滨冰雪大世界始创于1999年，是由哈尔滨市政府为迎接千年庆典神州世纪游活动，凭借哈尔滨的冰雪时节优势，而推出的大型冰雪艺术精品工程，展示了北方名城哈尔滨冰雪文化和冰雪旅游魅力。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=126.574286,45.806435&zoom=13&width=530&height=340&markers=126.574286,45.806435\"/></p>', '全国知名', 0, 300000, 10, 0, 'spot/2018/04/t0124e2b16d0731a7df.jpg', '黑龙江省哈尔滨市', '2018-04-14 05:28:54.000000', 3);
INSERT INTO `spots_spot` VALUES (3, '五大连池风景区', '1', '五大连池风景区，位于黑龙江省北部。“名山如画屏，珠带五湖清”，五大连池拔地而起的14座火山锥中间，一条蜿蜒曲折的河流，宛如一条蓝色绸带串连起大大小小5个堰塞湖，从火山锥之间穿流而过。除此之外，五大连池风景区范围内还分布着药泉湖、南北月牙泡、八卦湖、温泊等湖泊。柔美灵动的湖水中倒映着雄峻青山，山水辉映，构成一幅优美的中国传统山水画卷。先后荣获了世界地质公园、世界生物圈保护区、中国矿泉水之乡、中国著名火山之乡等称号。2004年2月3日，五大连池风景名胜区自然保护区被联合国教科文组织批准为全球首批世界地质公园之一。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=126.21034,48.670626&zoom=12&width=530&height=340&markers=126.21034,48.670626\"/></p>', '全国知名', 0, 355500, 20, 0, 'spot/2018/04/t01a95ddff2b3924bb9.jpg', '黑龙江省五大连池市', '2018-04-14 05:28:56.000000', 2);
INSERT INTO `spots_spot` VALUES (4, '张家界', '2', '张家界国家森林公园位于湖南省西北部张家界市境内，是1982年由国务院委托张家界国家森林公园旅游景区图国家计委批准成立的中国第一个国家森林公园，1992年12月因奇特的石英砂岩大峰林被联合国列入《世界自然遗产名录》，2004年2月被列入世界地质公园。\r\n公园自然风光以峰称奇、以谷显幽、以林见秀。其间有奇峰3000多座，这些石峰如人如兽、如器如物，形象逼真，气势壮观。峰间峡谷，溪流潺潺，浓荫蔽日。有“三千奇峰，八百秀水”之美称。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=110.485533,29.122816&zoom=13&width=530&height=340&markers=110.485533,29.122816\"/></p>', '全国知名', 0, 500000, 15, 0, 'spot/2018/04/t01b854d8de6ca13834.png', '张家界市', '2018-04-14 05:28:59.000000', 4);
INSERT INTO `spots_spot` VALUES (5, '都江堰', '2', '都江堰是世界文化遗产(2000年被联合国教科文组织列入\"世界文化遗产\"名录)，世界自然遗产(四川大熊猫栖息地)，全国重点文物保护单位，国家级风景名胜区，国家AAAAA级旅游景区。\r\n都江堰位于四川省成都市都江堰市城西，坐落在成都平原西部的岷江上，始建于秦昭王末年(约公元前256~前251) ，是蜀郡太守李冰父子在前人鳖灵开凿的基础上组织修建的大型水利工程，由分水鱼嘴、飞沙堰、宝瓶口等部分组成，两千多年来一直发挥着防洪灌溉的作用，使成都平原成为水旱从人、沃野千里的\"天府之国\"，至今灌区已达30余县市、面积近千万亩，是全世界迄今为止，年代最久、唯一留存、仍在一直使用，以无坝引水为特征的宏大水利工程，凝聚着中国古代汉族劳动人民勤劳、勇敢、智慧的结晶。\r\n都江堰风景区主要有伏龙观、二王庙、安澜索桥、玉垒关、离堆公园、玉垒山公园、玉女峰、灵岩寺、普照寺、翠月湖、都江堰水利工程等。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=103.638123,30.963805&zoom=12&width=530&height=340&markers=103.638123,30.963805\"/></p>', '全国知名', 0, 50000, 23, 0, 'spot/2018/04/t017fff5c384e775789.png', '都江堰', '2018-04-14 05:29:01.000000', 5);
INSERT INTO `spots_spot` VALUES (6, '长江三峡', '2', '长江三峡又名峡江或大三峡，位于中国重庆市、恩施州、宜昌市地区境内的长江干流上，西起重庆市奉节县的白帝城，东至湖北省宜昌市的南津关，全长193千米，由瞿塘峡、巫峡、西陵峡组成。\r\n长江三峡位于中国的腹地，属亚热带季风气候区，跨重庆奉节、重庆巫山、湖北巴东、湖北秭归、湖北宜昌。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=108.071004,30.293572&zoom=8&width=530&height=340&markers=108.071004,30.293572\"/></p>', '全国知名', 0, 900001, 23, 0, 'spot/2018/04/t01412cfc2af69a7af6.jpg', '长江', '2018-04-14 05:29:04.000000', 7);
INSERT INTO `spots_spot` VALUES (7, '古城区', '2', '丽江古城位于云南省丽江市古城区，又名大研古城，世界文化遗产丽江古城一共包括大研古城、束河古镇、白沙古镇三个部分。坐落在丽江坝中部，始建于宋末元初(公元13世纪后期)，地处云贵高原，面积为7.279平方公里。\r\n丽江古城内的街道依山傍水修建，以红色角砾岩铺就，有四方街、木府、五凤楼等景点。 丽江为第二批被批准的中国历史文化名城之一，是中国以整座古城申报世界文化遗产获得成功的两座古城之一。\r\n丽江古城有着多彩的地方民族习俗和娱乐活动，纳西古乐、东巴仪式、占卜文化、古镇酒吧以及纳西族火把节等，别具一格。丽江古城体现了中国古代城市建设的成就，是中国民居中具有鲜明特色和风格的类型之一。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=108.071004,30.293572&zoom=8&width=530&height=340&markers=108.071004,30.293572\"/></p>', '全国知名', 0, 100002, 56, 0, 'spot/2018/04/t01b5d3966dce8dc086.jpg', '丽江', '2018-04-14 05:29:07.000000', 8);
INSERT INTO `spots_spot` VALUES (8, '布达拉宫', '2', '布达拉宫（藏文：པོ་ཏ་ལ，藏语拼音：bo da la，威利：po ta la），坐落于中国西藏自治区的首府拉萨市区西北玛布日山上，是世界上海拔最高，集宫殿、城堡和寺院于一体的宏伟建筑，也是西藏最庞大、最完整的古代宫堡建筑群。 布达拉宫依山垒砌，群楼重叠，殿宇嵯峨，气势雄伟，是藏式古建筑的杰出代表，中华民族古建筑的精华之作，是第五套人民币50元纸币背面的风景图案[1]  。主体建筑分为白宫和红宫两部分。宫殿高200余米，外观13层，内为9层。布达拉宫前辟有布达拉宫广场，是世界上海拔最高的城市广场。 布达拉宫最初为吐蕃王朝赞普松赞干布为迎娶尺尊公主和文成公主而兴建。1645年（清顺治二年）五世达赖洛桑嘉措重建布达拉宫之后，成为历代达赖喇嘛冬宫居所，以及重大宗教和政治仪式举办地，也是供奉历世达赖喇嘛灵塔之地，旧时西藏政教合一的统治中心。 布达拉宫是藏传佛教的圣地，每年至此的朝圣者及旅游观光客不计其数。1961年3月，国务院列为首批全国重点文物保护单位；1994年12月，联合国教科文组织列其为世界文化遗产；2013年1月，国家旅游局又列为国家AAAAA级旅游景区；', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=91.134339,29.667806&zoom=14&width=530&height=340&markers=91.134339,29.667806\"/></p>', '全国知名', 0, 600000, 89, 0, 'spot/2018/04/t019f85c832a80dff89.jpg', '拉萨', '2018-04-14 05:29:17.000000', 9);
INSERT INTO `spots_spot` VALUES (9, '天安门', '2', '天安门，坐落在中华人民共和国首都北京市的中心、故宫的南端，与天安门广场以及人民英雄纪念碑、毛主席纪念堂、人民大会堂、中国国家博物馆隔长安街相望，占地面积4800平方米，以杰出的建筑艺术和特殊的政治地位为世人所瞩目。\r\n天安门是明清两代北京皇城的正门，始建于明朝永乐十五年(1417年)，最初名\"承天门\"，寓\"承天启运、受命于天\"之意。设计者为明代御用建筑匠师蒯祥。清朝顺治八年(1651年)更名为天安门。由城台和城楼两部分组成，有汉白玉石的须弥座，总高34.7米。天安门城楼长66米、宽37米。城台下有券门五阙，中间的券门最大，位于北京皇城中轴线上，过去只有皇帝才可以由此出入。正中门洞上方悬挂着毛泽东画像，两边分别是\"中华人民共和国万岁\"和\"世界人民大团结万岁\"的大幅标语。\r\n民国十四年(1925年)十月十日，故宫博物院成立，天安门开始对民众开放。1949年10月1日，在这里举行了中华人民共和国开国大典，由此被设计入国徽，并成为中华人民共和国的象征。1961年，中华人民共和国国务院公布为第一批全国重点文物保护单位之一。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=116.403042,39.911386&zoom=16&width=530&height=340&markers=116.403042,39.911386\"/></p>', '全国知名', 0, 10000000, 45, 0, 'spot/2018/04/t0147eaebfdee3f4c4a.png', '北京', '2018-04-14 05:29:23.000000', 10);
INSERT INTO `spots_spot` VALUES (10, '东方明珠', '1', '东方明珠广播电视塔(The Oriental Pearl Radio & TV Tower)是上海的标志性文化景观之一，位于浦东新区陆家嘴，塔高约468米。该建筑于1991年7月兴建，1995年5月投入使用，承担上海6套无线电视发射业务，地区覆盖半径80公里。\r\n东方明珠广播电视塔是国家首批AAAAA级旅游景区。塔内有太空舱、旋转餐厅、上海城市历史发展陈列馆等景观和设施，1995年被列入上海十大新景观之一。', '<p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=116.403042,39.911386&zoom=16&width=530&height=340&markers=116.403042,39.911386\"/></p>', '全国知名', 0, 60000, 56, 0, 'spot/2018/04/t014b1cc7479b23361c.jpg', '上海', '2018-04-14 05:29:26.000000', 11);
COMMIT;

-- ----------------------------
-- Table structure for spots_ticket
-- ----------------------------
DROP TABLE IF EXISTS `spots_ticket`;
CREATE TABLE `spots_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `category` varchar(20) NOT NULL,
  `desc` longtext NOT NULL,
  `detail` longtext NOT NULL,
  `tag` varchar(20) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `org_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `spots_ticket_org_id_66cf349d_fk_spots_spot_id` (`org_id`),
  CONSTRAINT `spots_ticket_org_id_66cf349d_fk_spots_spot_id` FOREIGN KEY (`org_id`) REFERENCES `spots_spot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spots_ticket
-- ----------------------------
BEGIN;
INSERT INTO `spots_ticket` VALUES (1, '哈尔滨冰雪大世界门票', 280, '1', '集哈尔滨冰雪大世界游览为一体的门票。', '全国知名', '100000', 55008, 30000, 'ticket/2018/04/t0124e2b16d0731a7df.jpg', '2018-04-13 21:04:00.000000', 2);
INSERT INTO `spots_ticket` VALUES (2, '五大连池风景区门票', 500, '1', '门票是集老黑山-冰洞-龙门石寨-温泊-南北泉-农家饭为一体的套票。', '全国知名', '225550', 10002, 22200, 'ticket/2018/04/t01a95ddff2b3924bb9.jpg', '2018-04-13 21:12:00.000000', 3);
INSERT INTO `spots_ticket` VALUES (3, '张家界国家森林公园', 100, '1', '张家界景区采用指纹IC卡电子门票，国家森林公园实行一票制（248元），两日内可持票游览杨家界、天子山、金鞭溪、黄石寨、袁家界。', '全国知名', '600000', 500001, 500000, 'ticket/2018/04/t01b854d8de6ca13834.png', '2018-04-13 21:18:00.000000', 4);
INSERT INTO `spots_ticket` VALUES (4, '都江堰门票', 90, '1', '1、景区门票价格：都江堰门票：90元\r\n2、都江堰半票：45元 购买对象（1、身高1.1-1.4米之间的儿童；2、60岁以上老人、残疾人凭本人有效证件；3、学生证、军官证）', '全国知名', '555000', 555501, 522000, 'ticket/2018/04/t017fff5c384e775789.png', '2018-04-13 21:39:00.000000', 5);
INSERT INTO `spots_ticket` VALUES (5, '丽江古城门票', 80, '1', '用于世界文化遗产丽江古城保护管理，丽江古城维护费的收费标准为:每人次80元，征收时间为:早上8:30--下午7:00。', '全国知名', '822000', 90001, 96330, 'ticket/2018/04/t01b5d3966dce8dc086.jpg', '2018-04-13 22:09:00.000000', 7);
INSERT INTO `spots_ticket` VALUES (6, '布达拉宫门票', 150, '2', '购票须知：布达拉宫实行预售与限售结合的卖票制，每天参观人数限制2300人（散客票约700张），每天下午5时后预售次日以后门票，每人限买4张，必须提前一天排队领取购票凭证，而且必须提供身份证号码，根据排队的先后，购票证上标明次日的参观时间，在布达拉宫的正大门持身份证购买门票进入。', '全国知名', '40000', 60011, 50000, 'ticket/2018/04/t019f85c832a80dff89.jpg', '2018-04-13 22:15:00.000000', 8);
INSERT INTO `spots_ticket` VALUES (7, '东方明珠', 180, '1', '观光+游船，上球体+陈列馆+浦江游览', '全国知名', '95500', 7006, 96300, 'ticket/2018/04/t014b1cc7479b23361c.jpg', '2018-04-13 22:30:00.000000', 10);
COMMIT;

-- ----------------------------
-- Table structure for users_banner
-- ----------------------------
DROP TABLE IF EXISTS `users_banner`;
CREATE TABLE `users_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `index` int(11) NOT NULL,
  `add_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_banner
-- ----------------------------
BEGIN;
INSERT INTO `users_banner` VALUES (1, '测试', 'banner/2018/04/3.jpg', 'http://127.0.0.1:8000/', 100, '2018-04-14');
INSERT INTO `users_banner` VALUES (2, 'http://127.0.0.1:8000/', 'banner/2018/04/2_LjF2z5J.jpg', 'http://127.0.0.1:8000/', 100, '2018-04-14');
COMMIT;

-- ----------------------------
-- Table structure for users_emailverifyrecord
-- ----------------------------
DROP TABLE IF EXISTS `users_emailverifyrecord`;
CREATE TABLE `users_emailverifyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(18) NOT NULL,
  `send_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile
-- ----------------------------
BEGIN;
INSERT INTO `users_userprofile` VALUES (1, 'pbkdf2_sha256$30000$kgHHZIvbjvUS$yC6AuBmhmkOV2yUPKenLd6K1e1F16TX/c9g2Apla/TM=', '2018-04-14 07:37:51.631572', 1, 'mukever', '', '', 'mukever@163.com', 1, 1, '2018-03-31 19:43:31.937740', '', NULL, 'female', '', NULL, 'image/2018/04/1.jpg');
INSERT INTO `users_userprofile` VALUES (2, 'pbkdf2_sha256$30000$Fru9KADvnOra$KK8YFpgwaIHRFnJ4FxMYp5+v4ECH48q6un6I9wiyYZI=', NULL, 0, '948433271@qq.com', '', '', '948433271@qq.com', 0, 0, '2018-04-01 22:18:50.500439', '', NULL, 'female', '', NULL, 'image?default.png');
INSERT INTO `users_userprofile` VALUES (3, 'pbkdf2_sha256$30000$RiuYPXbTV8jv$Sp0uGN4AVJvjbSUYpPGnYrsrHxM3awfgIxbdvlIogNM=', NULL, 0, 'zhouguangyao6@sina.com', '', '', 'zhouguangyao6@sina.com', 0, 0, '2018-04-10 15:16:01.997981', '', NULL, '', '', NULL, 'image/default.png');
COMMIT;

-- ----------------------------
-- Table structure for users_userprofile_groups
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofil_userprofile_id_a4496a80_fk_users_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_userprofile_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_permissions_userprofile_id_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_u_permission_id_393136b6_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `users_userprofil_userprofile_id_34544737_fk_users_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_u_permission_id_393136b6_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xadmin_bookmark
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookma_content_type_id_60941679_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookma_content_type_id_60941679_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xadmin_log
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
BEGIN;
INSERT INTO `xadmin_log` VALUES (1, '2018-04-14 05:45:05.366990', '127.0.0.1', '1', '测试', 'create', '已添加。', 12, 1);
INSERT INTO `xadmin_log` VALUES (2, '2018-04-14 05:48:03.979656', '127.0.0.1', '1', '测试', 'create', '已添加。', 21, 1);
INSERT INTO `xadmin_log` VALUES (3, '2018-04-14 05:48:26.298140', '127.0.0.1', '1', '测试', 'change', '修改 image 和 is_banner', 21, 1);
INSERT INTO `xadmin_log` VALUES (4, '2018-04-14 05:49:18.642417', '127.0.0.1', '1', '测试', 'create', '已添加。', 14, 1);
INSERT INTO `xadmin_log` VALUES (5, '2018-04-14 05:49:32.547324', '127.0.0.1', '2', 'http://127.0.0.1:8000/', 'create', '已添加。', 14, 1);
INSERT INTO `xadmin_log` VALUES (6, '2018-04-14 05:52:47.649953', '127.0.0.1', '2', '测试111', 'create', '已添加。', 21, 1);
INSERT INTO `xadmin_log` VALUES (7, '2018-04-14 06:02:23.277826', '127.0.0.1', '2', '测试111', 'change', '修改 price 和 image', 21, 1);
INSERT INTO `xadmin_log` VALUES (8, '2018-04-14 07:40:32.588922', '127.0.0.1', '12', 'UserMessage object', 'change', '修改 has_read', 23, 1);
INSERT INTO `xadmin_log` VALUES (9, '2018-04-14 07:54:07.511101', '127.0.0.1', '1', '测试', 'change', '修改 detail', 12, 1);
COMMIT;

-- ----------------------------
-- Table structure for xadmin_usersettings
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
BEGIN;
INSERT INTO `xadmin_usersettings` VALUES (1, 'dashboard:home:pos', '', 1);
COMMIT;

-- ----------------------------
-- Table structure for xadmin_userwidget
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
