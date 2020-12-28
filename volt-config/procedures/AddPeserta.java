package onlinetest.procedures;

import java.util.*;
import org.voltdb.*;

public class AddPeserta extends VoltProcedure {
  public final SQLStmt insertPeserta = new SQLStmt(
    "INSERT INTO PESERTA VALUES (?,?,?,0);"
  );
  public final SQLStmt insertDaftarSoal = new SQLStmt(
    "INSERT INTO DAFTAR_SOAL VALUES (?,?,?);"
  );
  public final SQLStmt selectSoal = new SQLStmt(
    "SELECT id_soal FROM SOAL;"
  );

  public VoltTable[] run(String username, String password, String name) throws VoltAbortException {
    voltQueueSQL(selectSoal);
    ArrayList<String> soalIdList = new ArrayList<String>();
    VoltTable[] resultsSoal = voltExecuteSQL();
    VoltTable soalTable = resultsSoal[0];
    
    for (int i = 0; i < soalTable.getRowCount(); i++) {
      VoltTableRow soalRow = soalTable.fetchRow(i);
      String idSoal = soalRow.getString(0);
      soalIdList.add(idSoal);
    }

    Collections.shuffle(soalIdList);

    for (int j = 0; j < soalIdList.size(); j++) {
      voltQueueSQL(insertDaftarSoal, username, soalIdList.get(j), j+1);
    }

    voltQueueSQL(insertPeserta, username, password, name);
    return voltExecuteSQL();
  }
}
