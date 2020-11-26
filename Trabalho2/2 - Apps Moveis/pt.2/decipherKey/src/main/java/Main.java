import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Random;

public class Main {
	public static void main(String[] args) throws Exception {

		String cipherKey = "8d127684cbc37c17616d806cf50473cc";

		String encryptedText = "5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=";

		String decrypt = AesImplementation.decrypt(encryptedText, cipherKey);

		System.out.println("The decoded password is :");
		System.out.println(decrypt);
	}
}
