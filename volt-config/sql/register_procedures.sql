load classes myproc.jar;

CREATE PROCEDURE FROM CLASS onlinetest.procedures.AddPeserta;
CREATE PROCEDURE FROM CLASS onlinetest.procedures.Login;
CREATE PROCEDURE FROM CLASS onlinetest.procedures.FinishTest;
CREATE PROCEDURE FROM CLASS onlinetest.procedures.AddSoal;
CREATE PROCEDURE FROM CLASS onlinetest.procedures.SelectPilihanBySoal;
CREATE PROCEDURE
  PARTITION ON TABLE DAFTAR_SOAL COLUMN username
  FROM CLASS onlinetest.procedures.SelectSoalByUrutan;
CREATE PROCEDURE
  PARTITION ON TABLE JAWABAN COLUMN username
  FROM CLASS onlinetest.procedures.SelectJawaban;
CREATE PROCEDURE
  PARTITION ON TABLE JAWABAN COLUMN username
  FROM CLASS onlinetest.procedures.SubmitJawaban;
CREATE PROCEDURE
  PARTITION ON TABLE JAWABAN COLUMN username
  FROM CLASS onlinetest.procedures.GetFinalScore;
