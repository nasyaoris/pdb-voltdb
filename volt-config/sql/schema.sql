CREATE TABLE PESERTA (
  username VARCHAR(64) NOT NULL,
  password VARCHAR(64) NOT NULL,
  name VARCHAR(128) NOT NULL,
  finished TINYINT DEFAULT '0',
  PRIMARY KEY(username)
);

CREATE TABLE SOAL (
  -- UUID
  id_soal VARCHAR(36) UNIQUE NOT NULL,
  soal VARCHAR(1024),
  kunci_jawaban VARCHAR(36) NOT NULL,
  PRIMARY KEY(id_soal)
);

CREATE TABLE PILIHAN (
  -- UUID
  id_pilihan VARCHAR(36) UNIQUE NOT NULL,
  -- UUID
  id_soal VARCHAR(36) NOT NULL,
  pilihan VARCHAR(1024),
  PRIMARY KEY(id_pilihan)
);

CREATE TABLE DAFTAR_SOAL (
  username VARCHAR(64) NOT NULL,
  -- UUID
  id_soal VARCHAR(36) NOT NULL,
  urutan INTEGER NOT NULL,
  CONSTRAINT pk_daftar_soal PRIMARY KEY(username, id_soal, urutan)
);
PARTITION TABLE DAFTAR_SOAL ON COLUMN username;

CREATE TABLE JAWABAN (
  username VARCHAR(64) NOT NULL,
  -- UUID
  id_soal VARCHAR(36) NOT NULL,
  -- UUID
  id_pilihan VARCHAR(36) NOT NULL,
  CONSTRAINT pk_jawaban PRIMARY KEY(username, id_soal)
);
PARTITION TABLE JAWABAN ON COLUMN username;
