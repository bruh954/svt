package pl.svietovit.app;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

/** Cała aplikacja to strona z folderu assets/www pokazana w WebView (działa bez internetu). */
public class MainActivity extends Activity {
    private static final String HOST = "appassets.androidplatform.net";
    private static final String START = "https://" + HOST + "/index.html";
    private WebView web;
    private TextToSpeech tts;
    private boolean ttsReady = false;

    private static final Map<String, String> MIME = new HashMap<>();
    static {
        MIME.put("html", "text/html"); MIME.put("js", "text/javascript"); MIME.put("css", "text/css");
        MIME.put("json", "application/json"); MIME.put("webmanifest", "application/manifest+json");
        MIME.put("wasm", "application/wasm"); MIME.put("zip", "application/zip"); MIME.put("py", "text/x-python");
        MIME.put("ttf", "font/ttf"); MIME.put("png", "image/png"); MIME.put("svg", "image/svg+xml");
    }

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);
        web = new WebView(this);
        setContentView(web);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setTextZoom(100);
        web.setBackgroundColor(0xFF0A1430);
        web.addJavascriptInterface(new Tts(), "AndroidTTS");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest req) {
                Uri u = req.getUrl();
                if (!HOST.equals(u.getHost())) return null;
                String path = u.getPath() == null ? "" : u.getPath();
                if (path.startsWith("/")) path = path.substring(1);
                if (path.isEmpty()) path = "index.html";
                try {
                    InputStream in = getAssets().open("www/" + path);
                    String ext = path.contains(".") ? path.substring(path.lastIndexOf('.') + 1).toLowerCase(Locale.ROOT) : "";
                    String mime = MIME.containsKey(ext) ? MIME.get(ext) : "application/octet-stream";
                    boolean text = mime.startsWith("text/") || mime.contains("json");
                    Map<String, String> headers = new HashMap<>();
                    headers.put("Access-Control-Allow-Origin", "*");
                    headers.put("Cache-Control", "no-cache");
                    return new WebResourceResponse(mime, text ? "utf-8" : null, 200, "OK", headers, in);
                } catch (IOException e) {
                    return new WebResourceResponse("text/plain", "utf-8", 404, "Not Found", new HashMap<String, String>(), null);
                }
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest req) {
                return !HOST.equals(req.getUrl().getHost());
            }
        });
        tts = new TextToSpeech(this, status -> ttsReady = status == TextToSpeech.SUCCESS);
        if (state == null) web.loadUrl(START); else web.restoreState(state);
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    public void onBackPressed() {
        web.evaluateJavascript("(function(){try{return window.__back?window.__back():false}catch(e){return false}})()",
                v -> { if (!"true".equals(v)) finish(); });
    }

    @Override
    protected void onDestroy() {
        if (tts != null) { tts.stop(); tts.shutdown(); }
        super.onDestroy();
    }

    /** Mowa: WebView nie ma speechSynthesis, więc strona woła systemowy syntezator. */
    private class Tts {
        @JavascriptInterface
        public void speak(String text, String lang, float rate) {
            if (!ttsReady || text == null) return;
            try {
                tts.setLanguage(Locale.forLanguageTag(lang));
                tts.setSpeechRate(rate);
                tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, "sv");
            } catch (Exception ignored) { }
        }
    }
}
