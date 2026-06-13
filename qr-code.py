
# QR Code Maker

import qrcode
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

print(
        Fore.CYAN
        + Style.BRIGHT
        + "=" * 35
        + "\n        QR Code Generator! \n"
        + "=" * 35
        + Style.RESET_ALL
    )

while True:
    try:
        menu = [
            "Simple QR Code",
            "QR with Logo in Center",
            "Exit"
        ]

        print("\n")

        for idx, option in enumerate(menu, start=1):
            print(f"{idx} - {option}")

        choice = int(input("Enter a Number: "))

        if choice == 1:
            data = input("\nEnter Text or Link: ")

            qr_code = qrcode.make(data)

            ask_name = input("\nEnter File Name without PNG: ")
            filename = f"{ask_name}.png"

            qr_code.save(filename)

            print(f"QR Code saved as {filename}")

            # Show QR Code using Photos
            qr_code.show()

        elif choice == 2:
            data = input("Enter Text or Link: ")

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            qr.add_data(data)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img = qr_img.convert("RGB")

            # Open Logo
            ask_logo_name = input("Enter Logo Name [without PNG]: ")
            logo = Image.open(f"{ask_logo_name}.png")

            # Resize Logo (20% of QR width)
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 5

            logo = logo.resize((logo_size, logo_size))

            # Calculate Center Position
            x = (qr_width - logo_size) // 2
            y = (qr_height - logo_size) // 2

            # Paste Logo
            qr_img.paste(logo, (x, y))

            # Save QR Code
            ask_name = input("\nEnter File Name without PNG: ")
            file_name = f"{ask_name}_with_logo.png"
            qr_img.save(file_name)

            print(f"QR Code saved as '{file_name}'")

            # Show QR Code
            qr_img.show()
        
        elif choice == 3:
            print("\nThanks for Using QR Code Generator.")
            break

        else:
            print("\nInvalid Input! Try Again...")
            continue

         # Instagram Credit Section
        print("\n" + Fore.CYAN + "=" * 35 + Fore.RESET)
        print(Fore.MAGENTA + "    📸 Follow on Instagram:" + Fore.RESET)
        print(Fore.MAGENTA + "     .---.  .---." + Fore.RESET)
        print(Fore.MAGENTA + "    |  _  \/  _  |" + Fore.RESET)
        print(
            Fore.MAGENTA
            + "    | | )    ( | |   "
            + Fore.YELLOW
            + Style.BRIGHT
            + "@Basantjangra79"
            + Style.RESET_ALL
        )
        print(Fore.MAGENTA + "    |  ~  /\  ~  |" + Fore.RESET)
        print(Fore.MAGENTA + "     '---'  '---'" + Fore.RESET)
        print(Fore.MAGENTA + "  📩 For Code: GitHub 🔗 in Bio  " + Fore.RESET)
        print(Fore.CYAN + "=" * 35 + "\n" + Fore.RESET)

        # # Pause before restarting the loop
        # input(Fore.BLUE + "Press Enter to Try again...[Ctrl + C] to Exit" + Fore.RESET)
        # print("\n" * 2)

    except KeyboardInterrupt:
        print("\n\nQR Code Generator Closed by User")
        break


    except ValueError:
        print("Invalid Input! Try Again...")
        continue
            
    except Exception as e:
        print("\nReport This Error to My Insta - @BasantJangra79\n[ERROR]: {e}\nTry Again...")
        continue
