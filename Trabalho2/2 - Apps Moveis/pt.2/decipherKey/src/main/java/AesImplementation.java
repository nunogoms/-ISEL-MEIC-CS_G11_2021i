import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class AesImplementation {
	public static String decrypt(String strToDecrypt, String secretKey) {


		byte[] b64Text = Base64.getDecoder().decode(strToDecrypt);
		byte[] keyBytes = hexToByte(secretKey);

		try {
			//PKCS5 is close to PKCS7 for small cases
			// The default is the same as AES/ECB/PKCS7Padding, which is used in the Smali files
			String encodingAlgorithm = "AES";

			SecretKeySpec secretKeySpec = new SecretKeySpec(keyBytes,encodingAlgorithm);

			Cipher cipher = Cipher.getInstance(encodingAlgorithm);

			cipher.init(Cipher.DECRYPT_MODE,secretKeySpec);

			return new String(cipher.doFinal(b64Text), StandardCharsets.UTF_8);
		} catch (Exception e) {
			System.out.println("Error while decrypting: " + e.toString());
		}
		return null;
	}

	public static byte[] hexToByte(String arg0){
		int var1 = arg0.length();
		byte [] auxByteArr = new byte[var1/2];
		for (int i = 0; i < var1; i+=2) {
			auxByteArr[i/2] = (byte) ((Character.digit(arg0.charAt(i),16)<<4) + Character.digit(arg0.charAt(i + 1),16));
		}
		return auxByteArr;
	}
}
