/*
SQLyog Professional v12.08 (64 bit)
MySQL - 5.7.19 : Database - hexun
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hexun` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `hexun`;

/*Table structure for table `lj_chengjiao` */

DROP TABLE IF EXISTS `lj_chengjiao`;

CREATE TABLE `lj_chengjiao` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `house_code` bigint(19) unsigned NOT NULL,
  `name` varchar(128) DEFAULT NULL COMMENT '房源名称',
  `region` varchar(128) DEFAULT NULL COMMENT '行政区域',
  `href` varchar(128) DEFAULT NULL COMMENT '房源链接',
  `style` varchar(64) DEFAULT NULL COMMENT '房源结构',
  `area` varchar(64) DEFAULT NULL COMMENT '小区',
  `orientation` varchar(32) DEFAULT NULL COMMENT '朝向',
  `decoration` varchar(32) DEFAULT NULL COMMENT '装修',
  `elevator` varchar(32) DEFAULT NULL COMMENT '电梯',
  `floor` varchar(32) DEFAULT NULL COMMENT '楼层高度',
  `build_year` varchar(32) DEFAULT NULL COMMENT '建造时间',
  `sign_time` varchar(16) DEFAULT NULL COMMENT '签约时间',
  `unit_price` decimal(15,5) DEFAULT NULL COMMENT '每平米单价',
  `total_price` decimal(15,5) DEFAULT NULL COMMENT '总价',
  `fangchan_class` varchar(16) DEFAULT NULL COMMENT '房产类型',
  `school` varchar(128) DEFAULT NULL COMMENT '周边学校',
  `subway` varchar(128) DEFAULT NULL COMMENT '周边地铁',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
