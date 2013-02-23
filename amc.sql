/*
Navicat MySQL Data Transfer

Source Server         : MIS
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : amc

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2013-02-23 14:33:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `credit`
-- ----------------------------
DROP TABLE IF EXISTS `credit`;
CREATE TABLE `credit` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `customerId` int(20) DEFAULT NULL,
  `ownMoney` varchar(100) DEFAULT NULL,
  `ownTime` char(19) DEFAULT NULL,
  `accumulateDebts` varchar(100) DEFAULT NULL,
  `beizhu` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of credit
-- ----------------------------

-- ----------------------------
-- Table structure for `customer`
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `userId` int(20) NOT NULL,
  `name` varchar(10) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `delorder`
-- ----------------------------
DROP TABLE IF EXISTS `delorder`;
CREATE TABLE `delorder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `orderId` int(20) DEFAULT NULL,
  `delPerson` varchar(10) DEFAULT NULL,
  `delTime` char(19) DEFAULT NULL,
  `driver` varchar(10) DEFAULT NULL,
  `driveTime` char(19) DEFAULT NULL,
  `delOrderStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of delorder
-- ----------------------------

-- ----------------------------
-- Table structure for `delorderinfo`
-- ----------------------------
DROP TABLE IF EXISTS `delorderinfo`;
CREATE TABLE `delorderinfo` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `delOrderId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `delNum` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of delorderinfo
-- ----------------------------

-- ----------------------------
-- Table structure for `depart`
-- ----------------------------
DROP TABLE IF EXISTS `depart`;
CREATE TABLE `depart` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `departName` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `employee`
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `userId` int(20) NOT NULL,
  `empName` varchar(10) DEFAULT NULL,
  `empDepartId` int(20) DEFAULT NULL,
  `empSex` varchar(2) DEFAULT NULL,
  `empAddress` varchar(60) DEFAULT NULL,
  `empPhone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `inaccount`
-- ----------------------------
DROP TABLE IF EXISTS `inaccount`;
CREATE TABLE `inaccount` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `productId` int(20) DEFAULT NULL,
  `inNum` int(100) DEFAULT NULL,
  `inTime` char(19) DEFAULT NULL,
  `inPerson` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inaccount
-- ----------------------------

-- ----------------------------
-- Table structure for `instockinform`
-- ----------------------------
DROP TABLE IF EXISTS `instockinform`;
CREATE TABLE `instockinform` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `supplierId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `productNum` int(100) DEFAULT NULL,
  `time` char(19) DEFAULT NULL,
  `status` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of instockinform
-- ----------------------------

-- ----------------------------
-- Table structure for `inventory`
-- ----------------------------
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE `inventory` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `productId` int(20) DEFAULT NULL,
  `number` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `lackorder`
-- ----------------------------
DROP TABLE IF EXISTS `lackorder`;
CREATE TABLE `lackorder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `orderInfoId` int(20) DEFAULT NULL,
  `lackNum` int(100) DEFAULT NULL,
  `lackPerson` varchar(10) DEFAULT NULL,
  `lackTime` char(19) DEFAULT NULL,
  `lackOrderStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lackorder
-- ----------------------------

-- ----------------------------
-- Table structure for `msg`
-- ----------------------------
DROP TABLE IF EXISTS `msg`;
CREATE TABLE `msg` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(500) DEFAULT NULL,
  `time` char(19) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `time` char(19) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `orderinfo`
-- ----------------------------
DROP TABLE IF EXISTS `orderinfo`;
CREATE TABLE `orderinfo` (
  `id` int(20) NOT NULL,
  `orderId` int(20) NOT NULL,
  `productId` int(20) NOT NULL,
  `orderNum` int(100) DEFAULT NULL,
  `orderInfoStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `outaccount`
-- ----------------------------
DROP TABLE IF EXISTS `outaccount`;
CREATE TABLE `outaccount` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `productId` int(20) DEFAULT NULL,
  `outNum` int(100) DEFAULT NULL,
  `outTime` char(19) DEFAULT NULL,
  `outPerson` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of outaccount
-- ----------------------------

-- ----------------------------
-- Table structure for `paybillaccount`
-- ----------------------------
DROP TABLE IF EXISTS `paybillaccount`;
CREATE TABLE `paybillaccount` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `purOrderId` int(20) DEFAULT NULL,
  `supplierId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `purNum` int(100) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` char(19) DEFAULT NULL,
  `payBillStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of paybillaccount
-- ----------------------------

-- ----------------------------
-- Table structure for `preorder`
-- ----------------------------
DROP TABLE IF EXISTS `preorder`;
CREATE TABLE `preorder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `orderId` int(20) DEFAULT NULL,
  `prePerson` varchar(10) DEFAULT NULL,
  `preOrderTime` char(19) DEFAULT NULL,
  `preOrderStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of preorder
-- ----------------------------

-- ----------------------------
-- Table structure for `preorderinfo`
-- ----------------------------
DROP TABLE IF EXISTS `preorderinfo`;
CREATE TABLE `preorderinfo` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `preOrderId` int(20) DEFAULT NULL,
  `orderInfoId` int(20) DEFAULT NULL,
  `preOrderNum` int(100) DEFAULT NULL,
  `preOrderPerson` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of preorderinfo
-- ----------------------------

-- ----------------------------
-- Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `productName` varchar(255) DEFAULT NULL,
  `originalId` varchar(255) DEFAULT NULL,
  `salePrice` varchar(20) DEFAULT NULL,
  `buyPrice` varchar(20) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `puraccount`
-- ----------------------------
DROP TABLE IF EXISTS `puraccount`;
CREATE TABLE `puraccount` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `purOrderId` int(20) DEFAULT NULL,
  `supplierId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `purNum` int(100) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` char(19) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of puraccount
-- ----------------------------

-- ----------------------------
-- Table structure for `purorder`
-- ----------------------------
DROP TABLE IF EXISTS `purorder`;
CREATE TABLE `purorder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `supplierId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `purNum` int(100) DEFAULT NULL,
  `purPerson` varchar(10) DEFAULT NULL,
  `purTime` char(19) DEFAULT NULL,
  `getTime` char(19) DEFAULT NULL,
  `purOrderStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of purorder
-- ----------------------------

-- ----------------------------
-- Table structure for `reminder`
-- ----------------------------
DROP TABLE IF EXISTS `reminder`;
CREATE TABLE `reminder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `delOrderId` int(20) DEFAULT NULL,
  `fare` varchar(100) DEFAULT NULL,
  `totalMoney` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` char(19) DEFAULT NULL,
  `recMoneyTime` char(19) DEFAULT NULL,
  `reminderStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reminder
-- ----------------------------

-- ----------------------------
-- Table structure for `reminderinfo`
-- ----------------------------
DROP TABLE IF EXISTS `reminderinfo`;
CREATE TABLE `reminderinfo` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `reminderId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `delNum` int(100) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reminderinfo
-- ----------------------------

-- ----------------------------
-- Table structure for `reorder`
-- ----------------------------
DROP TABLE IF EXISTS `reorder`;
CREATE TABLE `reorder` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `productId` int(20) DEFAULT NULL,
  `reorderNum` int(100) DEFAULT NULL,
  `reorderLevel` varchar(10) DEFAULT NULL,
  `reorderPerson` varchar(10) DEFAULT NULL,
  `reorderTime` char(19) DEFAULT NULL,
  `reorderStatus` char(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reorder
-- ----------------------------

-- ----------------------------
-- Table structure for `sellaccount`
-- ----------------------------
DROP TABLE IF EXISTS `sellaccount`;
CREATE TABLE `sellaccount` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `customerId` int(20) DEFAULT NULL,
  `reminderId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `sellNum` int(100) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` char(19) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sellaccount
-- ----------------------------

-- ----------------------------
-- Table structure for `shoppingcart`
-- ----------------------------
DROP TABLE IF EXISTS `shoppingcart`;
CREATE TABLE `shoppingcart` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `customerId` int(20) DEFAULT NULL,
  `productId` int(20) DEFAULT NULL,
  `orderNum` int(100) DEFAULT NULL,
  `money` varchar(500) DEFAULT NULL,
  `flag` int(1) DEFAULT NULL COMMENT '暂时不用到这个字段',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingcart
-- ----------------------------

-- ----------------------------
-- Table structure for `supplier`
-- ----------------------------
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE `supplier` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `supplierName` varchar(255) DEFAULT NULL,
  `supplierAdd` varchar(255) DEFAULT NULL,
  `supplierPhone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `t_order`
-- ----------------------------
DROP TABLE IF EXISTS `t_order`;
CREATE TABLE `t_order` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `customerId` int(20) NOT NULL,
  `receiver` varchar(20) DEFAULT NULL,
  `receiverAdd` varchar(255) DEFAULT NULL,
  `receiverPhone` varchar(11) DEFAULT NULL,
  `orderTime` char(19) DEFAULT NULL,
  `orderStatus` varchar(6) DEFAULT NULL,
  `unitedOrderId` varchar(23) DEFAULT NULL,
  `totalMoney` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) NOT NULL,
  `userPassword` varchar(255) NOT NULL,
  `userType` char(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
