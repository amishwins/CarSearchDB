drop table if exists `searchResult`;
drop table if exists `carOption`;
drop table if exists `car`;


CREATE TABLE IF NOT EXISTS `cars`.`car` (
  `carID` INT NOT NULL AUTO_INCREMENT,
  `manufacturer` VARCHAR(45) NOT NULL,
  `make` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`carID`),
  UNIQUE INDEX `carID_UNIQUE` (`manufacturer` ASC, `make` ASC, `year` ASC, `model` ASC))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `cars`.`carOption` (
  `optionID` INT NOT NULL AUTO_INCREMENT,
  `carID` INT NOT NULL,
  `optionDescription` TEXT NULL,
  PRIMARY KEY (`optionID`),
  UNIQUE INDEX `optionID_UNIQUE` (`optionID` ASC),
  INDEX `fksearchResultID_idx` (`carID` ASC),
  CONSTRAINT `fkcaroptioncarID`
    FOREIGN KEY (`carID`)
    REFERENCES `cars`.`car` (`carID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `cars`.`searchResult` (
  `searchResultID` INT NOT NULL AUTO_INCREMENT,
  `carID` INT NOT NULL,
  `dealership` VARCHAR(45) NOT NULL,
  `interestRate` DECIMAL(4,2) NULL,
  `monthly` DECIMAL(6,2) NULL,
  `numberOfMonths` INT NULL,
  `notes` TEXT NULL,
  PRIMARY KEY (`searchResultID`),
  UNIQUE INDEX `searchResultID_UNIQUE` (`searchResultID` ASC),
  INDEX `fkcarID_idx` (`carID` ASC),
  CONSTRAINT `fksearchresultcarID`
    FOREIGN KEY (`carID`)
    REFERENCES `cars`.`car` (`carID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;