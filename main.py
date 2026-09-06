import webview
import base64

def on_loaded(window):
    # Security Script: Right-Click aur F12 (Inspect) ko block karne ke liye
    js_code = """
        document.addEventListener('contextmenu', event => event.preventDefault());
        document.addEventListener('keydown', function(e) {
            if(e.keyCode == 123) { e.preventDefault(); return false; } // F12 Block
            if(e.ctrlKey && e.shiftKey && e.keyCode == 73) { e.preventDefault(); return false; } // Ctrl+Shift+I Block
        });
    """
    window.evaluate_js(js_code)

def main():
    # Tumhara URL yahan Base64 secret format mein chupa diya hai
    secret_url = base64.b64decode("aHR0cHM6Ly90ZWNobWF1cnlhLnB5dGhvbmFueXdoZXJlLmNvbQ==").decode("utf-8")

    window = webview.create_window(
        'BC Sir Hub - Premium', 
        secret_url, 
        width=1200, 
        height=800,
        min_size=(800, 600)
    )
    
    # Page load hone par security script inject hogi
    window.events.loaded += on_loaded
    
    # debug=False karne se koi bhi developer tools nahi khol payega
    webview.start(debug=False)

if __name__ == '__main__':
    main()
