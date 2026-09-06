import webview

def main():
    webview.create_window(
        'BC Sir Hub - Premium', 
        'https://techmaurya.pythonanywhere.com', 
        width=1200, 
        height=800,
        min_size=(800, 600)
    )
    webview.start()

if __name__ == '__main__':
    main()
