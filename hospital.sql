-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: tdtdatabase
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `DoctorInfo`
--

DROP TABLE IF EXISTS `DoctorInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DoctorInfo` (
  `doctorID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `specialty` varchar(100) DEFAULT NULL,
  `location` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`doctorID`),
  CONSTRAINT `doctorinfo_ibfk_1` FOREIGN KEY (`doctorID`) REFERENCES `User` (`userID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DoctorInfo`
--

LOCK TABLES `DoctorInfo` WRITE;
/*!40000 ALTER TABLE `DoctorInfo` DISABLE KEYS */;
INSERT INTO `DoctorInfo` VALUES (11,'Dr. Ox','Pulmonary','1-100'),(12,'Dr. Red','Cardiology','2-200'),(13,'Dr. Shepherd','General MD','1-101');
/*!40000 ALTER TABLE `DoctorInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PatientInfo`
--

DROP TABLE IF EXISTS `PatientInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PatientInfo` (
  `patientID` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` tinyint(4) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `height` tinyint(4) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `medicalhistory` varchar(1000) DEFAULT NULL,
  `insurance` varchar(20) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  PRIMARY KEY (`patientID`),
  CONSTRAINT `patientinfo_ibfk_1` FOREIGN KEY (`patientID`) REFERENCES `User` (`userID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PatientInfo`
--

LOCK TABLES `PatientInfo` WRITE;
/*!40000 ALTER TABLE `PatientInfo` DISABLE KEYS */;
INSERT INTO `PatientInfo` VALUES (1,'Charles Mandel',22,199,'Male',72,'20 Fake Street','311-243-2343','Diabetic','Medical Gold','1996-08-22'),(2,'Daniel Ladner',21,150,'Male',66,'32 NotSure Lane','347-222-1023','No Problems','Insurance Pro','1997-06-22'),(3,'Louis Pearson',21,200,'Male',68,'205 Bogus Blvd','347-901-1234','Insomnia','AARP','1997-03-22'),(4,'Jacob Roberts',47,255,'Male',77,'27 Terminator Drive','313-222-2015','Hernia','Medical Gold','1971-09-15'),(5,'Michelle Jacobs',30,135,'Female',64,'300 Butler Place','312-204-2200','Trouble hearing','Blue Cross','1988-07-23'),(6,'Dominic Klusek',21,160,'Male',69,'2800 Victory Blvd','376-304-2930','Not many issues','TrumpCare','1996-07-11'),(7,'Jamie Michels',28,122,'Female',62,'22 Saint-Ann Street','347-200-2093','Astmha','AARP','1990-03-10'),(8,'Nataly James',38,140,'Female',65,'685 Sequel Avenue','312-993-1295','Mood Swings','Blue Cross','1980-05-15'),(9,'Michael Jones',58,220,'Male',71,'1001 Jordan Street','917-233-2981','Arthritis','Medical Gold','1960-02-29'),(10,'Charles Mandela',88,175,'Male',73,'200 Secret Passage Way','902-199-1254','Dementia','AARP','1930-12-25');
/*!40000 ALTER TABLE `PatientInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescription`
--

DROP TABLE IF EXISTS `Prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Prescription` (
  `prescriptionID` int(11) NOT NULL AUTO_INCREMENT,
  `doctorID` int(11) DEFAULT NULL,
  `patientID` int(11) NOT NULL,
  `prescription` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prescriptionID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescription`
--

LOCK TABLES `Prescription` WRITE;
/*!40000 ALTER TABLE `Prescription` DISABLE KEYS */;
INSERT INTO `Prescription` VALUES (1,11,3,'Amoxicillin'),(2,12,7,'Inhaler'),(3,13,6,'Tylenol');
/*!40000 ALTER TABLE `Prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointment` (
  `appointmentID` int(11) NOT NULL AUTO_INCREMENT,
  `doctorID` int(11) DEFAULT NULL,
  `patientID` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  KEY `appointmentID` (`appointmentID`),
  KEY `doctorID` (`doctorID`),
  KEY `patientID` (`patientID`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`doctorID`) REFERENCES `doctorinfo` (`doctorID`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`patientID`) REFERENCES `patientinfo` (`patientID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,11,3,'2018-02-22 14:30:00'),(2,12,5,'2018-04-25 15:15:00'),(3,13,6,'2019-01-19 17:30:00');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `userType` varchar(20) DEFAULT NULL,
  `permissionLevel` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'ChaMan1','password','Patient',3),
                          (2,'DanLad1','password1','Patient',3),
                          (3,'LouPea1','password!','Patient',3),
                          (4,'JacRob1','drowssap','Patient',3),
                          (5,'MicJac1','drowssap!','Patient',3),
                          (6,'DomKlu1','drowssap1','Patient',3),
                          (7,'JamMic1','pass12!','Patient',3),
                          (8,'NatJam1','word13!','Patient',3),
                          (9,'MicJon1','ilovemycats','Patient',3),
                          (10,'ChaMan2','qwerty11','Patient',3),
                          (11,'DrOx','obamadid','Doctor',2),
                          (12,'DrRed','johnCena2020','Doctor',2),
                          (13,'DrShe','FreeKanye','Doctor',2),
                          (14, 'admin', 'admin','Admin',1);
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

-- Dump completed on 2018-04-26 19:40:36
