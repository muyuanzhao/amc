-- MySQL dump 10.13  Distrib 5.5.29, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: amc
-- ------------------------------------------------------
-- Server version	5.5.29-0ubuntu0.12.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `credit`
--

DROP TABLE IF EXISTS `credit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerId` int(11) DEFAULT NULL,
  `ownMoney` varchar(100) DEFAULT NULL,
  `ownTime` varchar(19) DEFAULT NULL,
  `accumulateDebt` varchar(100) DEFAULT NULL,
  `remark` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customerId` (`customerId`),
  CONSTRAINT `credit_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit`
--

LOCK TABLES `credit` WRITE;
/*!40000 ALTER TABLE `credit` DISABLE KEYS */;
/*!40000 ALTER TABLE `credit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `accountName` varchar(10) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userId` (`userId`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,1,'admin','buaa','1','clj@amc.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delorder`
--

DROP TABLE IF EXISTS `delorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) DEFAULT NULL,
  `delPerson` varchar(10) DEFAULT NULL,
  `delTime` varchar(19) DEFAULT NULL,
  `driver` varchar(10) DEFAULT NULL,
  `driveTime` varchar(19) DEFAULT NULL,
  `delOrderStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orderId` (`orderId`),
  CONSTRAINT `delorder_ibfk_1` FOREIGN KEY (`orderId`) REFERENCES `torder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delorder`
--

LOCK TABLES `delorder` WRITE;
/*!40000 ALTER TABLE `delorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `delorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delorderinfo`
--

DROP TABLE IF EXISTS `delorderinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delorderinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `delOrderId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `delNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delOrderId` (`delOrderId`),
  KEY `productId` (`productId`),
  CONSTRAINT `delorderinfo_ibfk_1` FOREIGN KEY (`delOrderId`) REFERENCES `delorder` (`id`),
  CONSTRAINT `delorderinfo_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delorderinfo`
--

LOCK TABLES `delorderinfo` WRITE;
/*!40000 ALTER TABLE `delorderinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `delorderinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `empName` varchar(10) DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userId` (`userId`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productId` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productId` (`productId`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,1,0),(2,2,10),(3,3,20),(4,4,30),(5,5,40),(6,6,50),(7,7,60),(8,8,70),(9,9,80),(10,10,90);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lackorder`
--

DROP TABLE IF EXISTS `lackorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lackorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderInfoId` int(11) DEFAULT NULL,
  `lackNum` int(11) DEFAULT NULL,
  `lackPerson` varchar(10) DEFAULT NULL,
  `lackTime` varchar(19) DEFAULT NULL,
  `lackOrderStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orderInfoId` (`orderInfoId`),
  CONSTRAINT `lackorder_ibfk_1` FOREIGN KEY (`orderInfoId`) REFERENCES `orderinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lackorder`
--

LOCK TABLES `lackorder` WRITE;
/*!40000 ALTER TABLE `lackorder` DISABLE KEYS */;
INSERT INTO `lackorder` VALUES (1,1,1,'xiaoshou','2013-03-13 05:36:30','lack'),(2,10,2,'xiaoshou','2013-03-13 05:36:41','lack');
/*!40000 ALTER TABLE `lackorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderinfo`
--

DROP TABLE IF EXISTS `orderinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `orderNum` int(11) DEFAULT NULL,
  `orderInfoStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orderId` (`orderId`),
  KEY `productId` (`productId`),
  CONSTRAINT `orderinfo_ibfk_1` FOREIGN KEY (`orderId`) REFERENCES `torder` (`id`),
  CONSTRAINT `orderinfo_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderinfo`
--

LOCK TABLES `orderinfo` WRITE;
/*!40000 ALTER TABLE `orderinfo` DISABLE KEYS */;
INSERT INTO `orderinfo` VALUES (1,2,1,1,'lack'),(2,2,2,1,'ready'),(3,2,7,1,'ready'),(4,2,8,1,'ready'),(5,2,9,1,'ready'),(6,2,10,1,'ready'),(7,2,5,1,'ready'),(8,2,4,1,'ready'),(9,2,3,1,'ready'),(10,3,1,2,'lack'),(11,3,2,2,'ready'),(12,3,7,2,'ready'),(13,3,8,2,'ready'),(14,3,9,1,'ready'),(15,3,10,1,'ready'),(16,3,5,1,'ready'),(17,3,4,1,'ready'),(18,3,3,2,'ready');
/*!40000 ALTER TABLE `orderinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paybillaccount`
--

DROP TABLE IF EXISTS `paybillaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paybillaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `purOrderId` int(11) DEFAULT NULL,
  `supplierId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `purNum` int(11) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` varchar(19) DEFAULT NULL,
  `payBillStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purOrderId` (`purOrderId`),
  KEY `supplierId` (`supplierId`),
  KEY `productId` (`productId`),
  CONSTRAINT `paybillaccount_ibfk_1` FOREIGN KEY (`purOrderId`) REFERENCES `purorder` (`id`),
  CONSTRAINT `paybillaccount_ibfk_2` FOREIGN KEY (`supplierId`) REFERENCES `supplier` (`id`),
  CONSTRAINT `paybillaccount_ibfk_3` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paybillaccount`
--

LOCK TABLES `paybillaccount` WRITE;
/*!40000 ALTER TABLE `paybillaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `paybillaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preorder`
--

DROP TABLE IF EXISTS `preorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `preorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) DEFAULT NULL,
  `prePerson` varchar(10) DEFAULT NULL,
  `preOrderTime` varchar(19) DEFAULT NULL,
  `preOrderStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orderId` (`orderId`),
  CONSTRAINT `preorder_ibfk_1` FOREIGN KEY (`orderId`) REFERENCES `torder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preorder`
--

LOCK TABLES `preorder` WRITE;
/*!40000 ALTER TABLE `preorder` DISABLE KEYS */;
INSERT INTO `preorder` VALUES (1,2,'xiaoshou','2013-03-13 05:36:30','ready'),(2,3,'xiaoshou','2013-03-13 05:36:41','ready');
/*!40000 ALTER TABLE `preorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preorderinfo`
--

DROP TABLE IF EXISTS `preorderinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `preorderinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `preOrderId` int(11) DEFAULT NULL,
  `orderInfoId` int(11) DEFAULT NULL,
  `preOrderNum` int(11) DEFAULT NULL,
  `preOrderPerson` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `preOrderId` (`preOrderId`),
  KEY `orderInfoId` (`orderInfoId`),
  CONSTRAINT `preorderinfo_ibfk_1` FOREIGN KEY (`preOrderId`) REFERENCES `preorder` (`id`),
  CONSTRAINT `preorderinfo_ibfk_2` FOREIGN KEY (`orderInfoId`) REFERENCES `orderinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preorderinfo`
--

LOCK TABLES `preorderinfo` WRITE;
/*!40000 ALTER TABLE `preorderinfo` DISABLE KEYS */;
INSERT INTO `preorderinfo` VALUES (1,1,2,1,'xiaoshou'),(2,1,3,1,'xiaoshou'),(3,1,4,1,'xiaoshou'),(4,1,5,1,'xiaoshou'),(5,1,6,1,'xiaoshou'),(6,1,7,1,'xiaoshou'),(7,1,8,1,'xiaoshou'),(8,1,9,1,'xiaoshou'),(9,2,11,2,'xiaoshou'),(10,2,12,2,'xiaoshou'),(11,2,13,2,'xiaoshou'),(12,2,14,1,'xiaoshou'),(13,2,15,1,'xiaoshou'),(14,2,16,1,'xiaoshou'),(15,2,17,1,'xiaoshou'),(16,2,18,2,'xiaoshou');
/*!40000 ALTER TABLE `preorderinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productName` varchar(255) DEFAULT NULL,
  `salePrice` varchar(20) DEFAULT NULL,
  `buyPrice` varchar(20) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'product_0','100.99','60.99','product','0'),(2,'product_1','110.99','70.99','product','0'),(3,'product_2','120.99','80.99','product','0'),(4,'product_3','130.99','90.99','product','0'),(5,'product_4','140.99','100.99','product','0'),(6,'product_5','150.99','110.99','product','0'),(7,'product_6','160.99','120.99','product','0'),(8,'product_7','170.99','130.99','product','0'),(9,'product_8','180.99','140.99','product','0'),(10,'product_9','190.99','150.99','product','0');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puraccount`
--

DROP TABLE IF EXISTS `puraccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `puraccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `purOrderId` int(11) DEFAULT NULL,
  `supplierId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `purNum` int(11) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` varchar(19) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purOrderId` (`purOrderId`),
  KEY `supplierId` (`supplierId`),
  KEY `productId` (`productId`),
  CONSTRAINT `puraccount_ibfk_1` FOREIGN KEY (`purOrderId`) REFERENCES `purorder` (`id`),
  CONSTRAINT `puraccount_ibfk_2` FOREIGN KEY (`supplierId`) REFERENCES `supplier` (`id`),
  CONSTRAINT `puraccount_ibfk_3` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puraccount`
--

LOCK TABLES `puraccount` WRITE;
/*!40000 ALTER TABLE `puraccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `puraccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purorder`
--

DROP TABLE IF EXISTS `purorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supplierId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `purNum` int(11) DEFAULT NULL,
  `purPerson` varchar(10) DEFAULT NULL,
  `purTime` varchar(19) DEFAULT NULL,
  `getTime` varchar(19) DEFAULT NULL,
  `purOrderStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supplierId` (`supplierId`),
  KEY `productId` (`productId`),
  CONSTRAINT `purorder_ibfk_1` FOREIGN KEY (`supplierId`) REFERENCES `supplier` (`id`),
  CONSTRAINT `purorder_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purorder`
--

LOCK TABLES `purorder` WRITE;
/*!40000 ALTER TABLE `purorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `purorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reminder`
--

DROP TABLE IF EXISTS `reminder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reminder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `delOrderId` int(11) DEFAULT NULL,
  `fare` varchar(100) DEFAULT NULL,
  `totalMoney` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` varchar(19) DEFAULT NULL,
  `recMoneyTime` varchar(19) DEFAULT NULL,
  `reminderStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delOrderId` (`delOrderId`),
  CONSTRAINT `reminder_ibfk_1` FOREIGN KEY (`delOrderId`) REFERENCES `delorder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reminder`
--

LOCK TABLES `reminder` WRITE;
/*!40000 ALTER TABLE `reminder` DISABLE KEYS */;
/*!40000 ALTER TABLE `reminder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reminderinfo`
--

DROP TABLE IF EXISTS `reminderinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reminderinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reminderId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `delNum` int(11) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reminderId` (`reminderId`),
  KEY `productId` (`productId`),
  CONSTRAINT `reminderinfo_ibfk_1` FOREIGN KEY (`reminderId`) REFERENCES `reminder` (`id`),
  CONSTRAINT `reminderinfo_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reminderinfo`
--

LOCK TABLES `reminderinfo` WRITE;
/*!40000 ALTER TABLE `reminderinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `reminderinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reorder`
--

DROP TABLE IF EXISTS `reorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productId` int(11) DEFAULT NULL,
  `reorderNum` int(11) DEFAULT NULL,
  `reorderLevel` varchar(10) DEFAULT NULL,
  `reorderPerson` varchar(10) DEFAULT NULL,
  `reorderTime` varchar(19) DEFAULT NULL,
  `reorderStatus` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productId` (`productId`),
  CONSTRAINT `reorder_ibfk_1` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reorder`
--

LOCK TABLES `reorder` WRITE;
/*!40000 ALTER TABLE `reorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `reorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellaccount`
--

DROP TABLE IF EXISTS `sellaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerId` int(11) DEFAULT NULL,
  `reminderId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `sellNum` int(11) DEFAULT NULL,
  `money` varchar(100) DEFAULT NULL,
  `accountPerson` varchar(10) DEFAULT NULL,
  `accountTime` varchar(19) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customerId` (`customerId`),
  KEY `reminderId` (`reminderId`),
  KEY `productId` (`productId`),
  CONSTRAINT `sellaccount_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customer` (`id`),
  CONSTRAINT `sellaccount_ibfk_2` FOREIGN KEY (`reminderId`) REFERENCES `reminder` (`id`),
  CONSTRAINT `sellaccount_ibfk_3` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellaccount`
--

LOCK TABLES `sellaccount` WRITE;
/*!40000 ALTER TABLE `sellaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppingcart`
--

DROP TABLE IF EXISTS `shoppingcart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shoppingcart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerId` int(11) DEFAULT NULL,
  `productId` int(11) DEFAULT NULL,
  `orderNum` int(11) DEFAULT NULL,
  `money` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customerId` (`customerId`),
  KEY `productId` (`productId`),
  CONSTRAINT `shoppingcart_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customer` (`id`),
  CONSTRAINT `shoppingcart_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingcart`
--

LOCK TABLES `shoppingcart` WRITE;
/*!40000 ALTER TABLE `shoppingcart` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoppingcart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supplierName` varchar(255) DEFAULT NULL,
  `supplierAdd` varchar(255) DEFAULT NULL,
  `supplierPhone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `torder`
--

DROP TABLE IF EXISTS `torder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `torder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerId` int(11) DEFAULT NULL,
  `receiver` varchar(20) DEFAULT NULL,
  `receiverAdd` varchar(255) DEFAULT NULL,
  `receiverPhone` varchar(11) DEFAULT NULL,
  `orderTime` varchar(19) DEFAULT NULL,
  `orderStatus` varchar(6) DEFAULT NULL,
  `totalMoney` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customerId` (`customerId`),
  CONSTRAINT `torder_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `torder`
--

LOCK TABLES `torder` WRITE;
/*!40000 ALTER TABLE `torder` DISABLE KEYS */;
INSERT INTO `torder` VALUES (1,1,'admin','buaa','1','2013-03-09 05:43:13','ready','680.81','0'),(2,1,'admin','buaa','1','2013-03-13 05:36:30','lack','331.91','0'),(3,1,'admin','buaa','1','2013-03-13 05:36:41','lack','497.86','0');
/*!40000 ALTER TABLE `torder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(80) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `role` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin@amc.com','admin','1');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-03-13 13:37:02
