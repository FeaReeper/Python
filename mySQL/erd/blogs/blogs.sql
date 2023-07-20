-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema blogs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema blogs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blogs` DEFAULT CHARACTER SET utf8 ;
USE `blogs` ;

-- -----------------------------------------------------
-- Table `blogs`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`blogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`blogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`admins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_blogs_blogs1_idx` (`blog_id` ASC) VISIBLE,
  INDEX `fk_users_has_blogs_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_blogs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `blogs`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `info` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `admin_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_admins1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_posts_blogs1_idx` (`blog_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `blogs`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `comment` VARCHAR(255) NULL,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `blogs`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`files` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `file` BLOB NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `post_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_files_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_files_admins1_idx` (`admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_files_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `blogs`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_files_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs`.`page_views`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs`.`page_views` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blogs_id` INT NOT NULL,
  `view_time` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_blogs_blogs2_idx` (`blogs_id` ASC) VISIBLE,
  INDEX `fk_users_has_blogs_users2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_blogs_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs2`
    FOREIGN KEY (`blogs_id`)
    REFERENCES `blogs`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
