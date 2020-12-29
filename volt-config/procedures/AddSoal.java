package onlinetest.procedures;

import java.util.UUID;
import org.voltdb.*;

public class AddSoal extends VoltProcedure {
  public final SQLStmt insertSoal = new SQLStmt(
    "INSERT INTO SOAL VALUES (?,?,?);"
  );
  public final SQLStmt insertPilihan = new SQLStmt(
    "INSERT INTO PILIHAN VALUES (?,?,?);"
  );

  public VoltTable[] run(String soal, String pilihan1, String pilihan2, String pilihan3, String pilihan4, int kunci) throws VoltAbortException {
    String id_soal = UUID.randomUUID().toString();
    String id_pilihan1 = UUID.randomUUID().toString();
    String id_pilihan2 = UUID.randomUUID().toString();
    String id_pilihan3 = UUID.randomUUID().toString();
    String id_pilihan4 = UUID.randomUUID().toString();
    String[] daftar_pilihan = {id_pilihan1, id_pilihan2, id_pilihan3, id_pilihan4};
    String kunci_jawaban = daftar_pilihan[kunci];

    voltQueueSQL(insertPilihan, id_pilihan1, id_soal, pilihan1);
    voltQueueSQL(insertPilihan, id_pilihan2, id_soal, pilihan2);
    voltQueueSQL(insertPilihan, id_pilihan3, id_soal, pilihan3);
    voltQueueSQL(insertPilihan, id_pilihan4, id_soal, pilihan4);
    voltQueueSQL(insertSoal, id_soal, soal, kunci_jawaban);
    return voltExecuteSQL();
  }
}
