import os

from chatlas import ChatGoogle

from .prompt import generate_prompt


def main():
    client = ChatGoogle(
        model="gemini-2.5-pro-preview-05-06",
        api_key=os.environ["GOOGLE_GEMINI_PRO_API_KEY"],
        system_prompt=generate_prompt(),
    )

    advertisements = [
        """ሁል የተሟላለት ቅንጡ የመኖሪያ ቤት ኪራይ ሲምሲ ኮፓውንድ ውስጥ ካሬ ሜትር 600
    መኝታ ቤት 6 ሳሎን 2 ኪችን2 ሻውር ሽንት ቤት 5 በቂ የመናፈሻ ስፍራ መኪና ማቆሚያ 6
    ዋጋ140 ሽ ኮሚሽን 10% 0911067686x""",
        """betam konjo tsidit bilo yetesera condominum bet be lideta kondominium andegna fok lay hulum neger yalekelet konjo bet mulu ceramic yetesera kichin kabinet yalew konjo bet new 1 mignta 2 metatebiaya 5.5 sifatu 120 kare le nigid mehon yichilal. Bank bidir enamechachalen. እስከ 50,000ብር የሚካራይ ጋዢ በ0912403669 ይደውሉልን. Abebe https://t.me/broker_abebe""",
    ]

    response = client.chat(advertisements[0])

    print(response.get_content())

if __name__ == "__main__":
    main()