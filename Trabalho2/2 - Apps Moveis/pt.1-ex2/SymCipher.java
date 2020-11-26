import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Random;

public class SymCipher {
  public static void main(String[] args) throws Exception {
    byte[] plaintext = "The quick brown fox jumps over the lazy dog".getBytes();
    byte[] ciphertext;

    // get random 8 bytes
    byte[] rawkey = new byte[8];
    new Random().nextBytes(rawkey);

    // KeySpec is a way to build a key from a byte[]
    // and the name of the algorithm where the key is to be used
    SecretKeySpec key = new SecretKeySpec(rawkey, "DES");

    // DES cipher in CBC mode and PKCS#5 padding
    Cipher cipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
    // init in encrypt mode and set the symmetric key
    cipher.init(Cipher.ENCRYPT_MODE, key);

    // encrypt plaintext
    ciphertext = cipher.doFinal(plaintext);
    // save initial vector used during encryption
    byte[] iv = cipher.getIV();

    // init in decrypt mode and set the symmetric key
    cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(iv));

    // decrypt ciphertext
    byte[] newPlainText = cipher.doFinal(ciphertext);

    // show message
    System.out.println(new String(newPlainText));
  }
}
