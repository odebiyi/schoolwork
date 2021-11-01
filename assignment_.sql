-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2021 at 11:25 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment_`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidate`
--

CREATE TABLE `candidate` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `telephone_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candidate`
--

INSERT INTO `candidate` (`id`, `firstname`, `surname`, `telephone_number`) VALUES
(1, 'BEN', 'BENNY', 809513123),
(2, 'JAMES', 'JONES', 981213411),
(3, 'JI JUAM', 'ALLEN', 909989888),
(9088767543, 'FOSO', 'ALLIA', 901121545),
(9088767544, 'JOAN', 'JULIET', 892145122);

-- --------------------------------------------------------

--
-- Table structure for table `candidate_interviews`
--

CREATE TABLE `candidate_interviews` (
  `candidate_id` bigint(20) NOT NULL,
  `interviews_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candidate_interviews`
--

INSERT INTO `candidate_interviews` (`candidate_id`, `interviews_id`) VALUES
(1, 2),
(2, 3),
(3, 1),
(3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `candidate_skills`
--

CREATE TABLE `candidate_skills` (
  `candidate_id` bigint(20) NOT NULL,
  `skills_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candidate_skills`
--

INSERT INTO `candidate_skills` (`candidate_id`, `skills_id`) VALUES
(1, 1),
(1, 2),
(1, 5),
(2, 4),
(3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `id` bigint(20) NOT NULL,
  `dept_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`id`, `dept_name`) VALUES
(1, 'Technology Innovation and Development'),
(2, 'QUALITY ASSURANCE'),
(3, 'PROJECT MANAGEMENT'),
(4, 'PRODUCT MANAGER'),
(5, 'DEVOPS');

-- --------------------------------------------------------

--
-- Table structure for table `department_interviews`
--

CREATE TABLE `department_interviews` (
  `department_id` bigint(20) NOT NULL,
  `interviews_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department_interviews`
--

INSERT INTO `department_interviews` (`department_id`, `interviews_id`) VALUES
(3, 1),
(3, 4),
(4, 3),
(5, 2),
(5, 7);

-- --------------------------------------------------------

--
-- Table structure for table `interview`
--

CREATE TABLE `interview` (
  `id` bigint(20) NOT NULL,
  `position_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `interview`
--

INSERT INTO `interview` (`id`, `position_id`) VALUES
(3, 1),
(1, 2),
(4, 2),
(7, 2),
(2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `position`
--

CREATE TABLE `position` (
  `id` bigint(20) NOT NULL,
  `position_name` varchar(255) DEFAULT NULL,
  `position_type` varchar(255) DEFAULT NULL,
  `skill_required_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `position`
--

INSERT INTO `position` (`id`, `position_name`, `position_type`, `skill_required_id`) VALUES
(1, 'MANAGER', 'MANAGER', 5),
(2, 'ASSISTANT MANAGER', 'ASSISTANT MANAGER', 1),
(3, 'JUNIOR MANAGER', 'JUNIOR MANAGER', 2),
(4, 'ENTRY MANAGER', 'ENTRY MANAGER', 3),
(5, 'JANITOR', 'JANITOR', 1);

-- --------------------------------------------------------

--
-- Table structure for table `skill`
--

CREATE TABLE `skill` (
  `id` bigint(20) NOT NULL,
  `skill_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skill`
--

INSERT INTO `skill` (`id`, `skill_name`) VALUES
(1, 'Coding and Scripting in Java'),
(2, 'Testing using Jmeter'),
(3, 'Performance Testing using Jmeter'),
(4, 'WEB DEVELOPMENT USING CSS'),
(5, 'CI/CD USING AWS');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `candidate_interviews`
--
ALTER TABLE `candidate_interviews`
  ADD UNIQUE KEY `UK_nnt4lfnmx1rymkj8k38x0sal1` (`interviews_id`),
  ADD KEY `FK5qvl2lka8elpl8s6dui9kvprw` (`candidate_id`);

--
-- Indexes for table `candidate_skills`
--
ALTER TABLE `candidate_skills`
  ADD UNIQUE KEY `UK_ejwec7hb0uwlw7prdyof9qbxn` (`skills_id`),
  ADD KEY `FKneg4g0bpemx5jjfnjly3wxmhi` (`candidate_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `department_interviews`
--
ALTER TABLE `department_interviews`
  ADD UNIQUE KEY `UK_chy2i2bjyv6cjrdoq0o1dig3j` (`interviews_id`),
  ADD KEY `FKpftf4sfihxiqn556ag8pvu68k` (`department_id`);

--
-- Indexes for table `interview`
--
ALTER TABLE `interview`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKlbxm7p98trn9hes0bchfemcuy` (`position_id`);

--
-- Indexes for table `position`
--
ALTER TABLE `position`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK7ta8oveic8w4289y2saruwmef` (`skill_required_id`);

--
-- Indexes for table `skill`
--
ALTER TABLE `skill`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidate`
--
ALTER TABLE `candidate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9088767545;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `interview`
--
ALTER TABLE `interview`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `position`
--
ALTER TABLE `position`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `skill`
--
ALTER TABLE `skill`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `candidate_interviews`
--
ALTER TABLE `candidate_interviews`
  ADD CONSTRAINT `FK5qvl2lka8elpl8s6dui9kvprw` FOREIGN KEY (`candidate_id`) REFERENCES `candidate` (`id`),
  ADD CONSTRAINT `FK94ehw637gb3plb13ixhuuw3qw` FOREIGN KEY (`interviews_id`) REFERENCES `interview` (`id`);

--
-- Constraints for table `candidate_skills`
--
ALTER TABLE `candidate_skills`
  ADD CONSTRAINT `FK6ubfe6ggu0f65u0db7crl04wu` FOREIGN KEY (`skills_id`) REFERENCES `skill` (`id`),
  ADD CONSTRAINT `FKneg4g0bpemx5jjfnjly3wxmhi` FOREIGN KEY (`candidate_id`) REFERENCES `candidate` (`id`);

--
-- Constraints for table `department_interviews`
--
ALTER TABLE `department_interviews`
  ADD CONSTRAINT `FK9reug7dyfn3vrbd6snnoq0p5o` FOREIGN KEY (`interviews_id`) REFERENCES `interview` (`id`),
  ADD CONSTRAINT `FKpftf4sfihxiqn556ag8pvu68k` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);

--
-- Constraints for table `interview`
--
ALTER TABLE `interview`
  ADD CONSTRAINT `FKlbxm7p98trn9hes0bchfemcuy` FOREIGN KEY (`position_id`) REFERENCES `position` (`id`);

--
-- Constraints for table `position`
--
ALTER TABLE `position`
  ADD CONSTRAINT `FK7ta8oveic8w4289y2saruwmef` FOREIGN KEY (`skill_required_id`) REFERENCES `skill` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
