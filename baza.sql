

CREATE TABLE `python_app`.`kanjii` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `unicode` int(11) DEFAULT NULL,
  `nazwa` varchar(45) DEFAULT NULL,
  `znaczenie` varchar(45) DEFAULT NULL,
  PRIMARY KEY `idkanji_UNIQUE` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e80', 'kami', 'tortoise');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e94', 'go', 'piec');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e8c', 'ni', 'dwa');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e83', 'shinu', 'pies');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e84', 'yuki', 'snieg');

INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e00', 'ichi', 'jeden');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e09', 'san', 'trzy');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e0a', 'jama', 'gora');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e2d', 'naki', 'środek');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4eba', 'hito', 'człowiek');

INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'51fa', 'deru', 'wyjscie');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e02', 'ki', 'oddech');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4e03', 'nana', 'siedem');

INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'529b', 'chikara', 'siła');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4f1e', 'kasa', 'parasol');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'5186', 'yen', 'jen');
INSERT INTO `python_app`.`kanjii` ( `unicode`, `nazwa`, `znaczenie`) VALUES ( X'4f50', 'nani', 'kto');
