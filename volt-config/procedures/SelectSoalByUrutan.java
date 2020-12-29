package onlinetest.procedures;

import org.voltdb.*;

public class SelectSoalByUrutan extends VoltProcedure {
  public final SQLStmt selectDaftarSoal = new SQLStmt(
    "SELECT id_soal FROM DAFTAR_SOAL WHERE username=? AND urutan=?;"
  );
  public final SQLStmt selectSoal = new SQLStmt(
    "SELECT id_soal, soal FROM SOAL WHERE id_soal=?;"
  );

  public VoltTable[] run(String username, int urutan) throws VoltAbortException {
    voltQueueSQL(selectDaftarSoal, username, urutan);
    VoltTable[] resultDaftarSoal = voltExecuteSQL();
    VoltTable daftarSoalTable = resultDaftarSoal[0];
    VoltTableRow daftarSoalRow = daftarSoalTable.fetchRow(0);
    String idSoal = daftarSoalRow.getString(0);
    voltQueueSQL(selectSoal, idSoal);
    return voltExecuteSQL();
  }
}
