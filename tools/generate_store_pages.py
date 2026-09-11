#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
UPDATED = "2026-09-11"

LANGS = {
    "ko": {"label": "한국어", "html_lang": "ko"},
    "en": {"label": "English", "html_lang": "en"},
    "ja": {"label": "日本語", "html_lang": "ja"},
    "zh": {"label": "中文", "html_lang": "zh-CN"},
}

NAV = {
    "ko": {"privacy": "개인정보처리방침", "support": "지원", "terms": "이용약관", "data": "데이터 및 계정", "info": "앱 정보"},
    "en": {"privacy": "Privacy", "support": "Support", "terms": "Terms", "data": "Data & Account", "info": "App Info"},
    "ja": {"privacy": "プライバシー", "support": "サポート", "terms": "利用規約", "data": "データとアカウント", "info": "アプリ情報"},
    "zh": {"privacy": "隐私", "support": "支持", "terms": "使用条款", "data": "数据与账户", "info": "应用信息"},
}

COMMON = {
    "ko": {
        "app": "Adelie Pages",
        "operator": "Adelie Draw (아델리드로우)",
        "updated": "시행/최종 업데이트",
        "contact": "문의",
        "address": "주소",
        "address_value": "서울특별시 동대문구 천호대로55길 11, 02597, 대한민국",
        "email": "이메일",
        "phone": "전화",
        "contents": "문서 목차",
        "home": "Adelie Pages 홈",
    },
    "en": {
        "app": "Adelie Pages",
        "operator": "Adelie Draw",
        "updated": "Effective / last updated",
        "contact": "Contact",
        "address": "Address",
        "address_value": "11, Cheonho-daero 55-gil, Dongdaemun-gu, Seoul 02597, Republic of Korea",
        "email": "Email",
        "phone": "Phone",
        "contents": "Contents",
        "home": "Adelie Pages home",
    },
    "ja": {
        "app": "Adelie Pages",
        "operator": "Adelie Draw（アデリードロー）",
        "updated": "施行・最終更新",
        "contact": "お問い合わせ",
        "address": "住所",
        "address_value": "大韓民国 02597 ソウル特別市 東大門区 千戸大路55キル11",
        "email": "メール",
        "phone": "電話",
        "contents": "目次",
        "home": "Adelie Pages ホーム",
    },
    "zh": {
        "app": "Adelie Pages",
        "operator": "Adelie Draw（阿德利绘）",
        "updated": "生效/最后更新",
        "contact": "联系",
        "address": "地址",
        "address_value": "韩国首尔特别市东大门区千户大路55街11号，邮编02597",
        "email": "电子邮件",
        "phone": "电话",
        "contents": "目录",
        "home": "Adelie Pages 首页",
    },
}


def p(text):
    return ("p", text)


def ul(*items):
    return ("ul", list(items))


def note(text):
    return ("note", text)


PAGES = {
    "privacy": {
        "ko": {
            "title": "개인정보처리방침",
            "display": "개인정보\n처리방침",
            "summary": "Adelie Pages가 어떤 데이터를 기기 안에서 처리하고, 사진·알림·구매 기능을 사용할 때 어떤 외부 서비스와 통신할 수 있는지 설명합니다.",
            "sections": [
                ("적용 범위", [p("이 방침은 Adelie Draw가 제공하는 Adelie Pages 모바일 앱(iOS·Android)에 적용됩니다. 현재 공개 준비 중인 앱은 별도의 Adelie 계정 생성이나 로그인을 제공하지 않습니다.")]),
                ("기기 안에서 처리되는 데이터", [p("페이지, 초안, 템플릿, 다이어리 기록, 즐겨찾기·최근 사용 정보, 알림 설정과 사용자가 불러온 사진의 앱 전용 사본은 기기 로컬 저장소에 저장될 수 있습니다."), p("이 정보는 사용자가 저장·편집 기능을 이용한다는 이유만으로 Adelie Draw 서버에 업로드되지 않습니다. 현재 빌드에는 Adelie 계정 기반 클라우드 백업이 없습니다."), ul("사용자가 만든 페이지·초안·텍스트와 배치 정보", "사용자가 갤러리에서 선택한 사진의 앱 전용 사본", "알림 사용 여부, 알림 시각, 시간대 등 설정", "앱에서 저장한 내보내기 파일과 로컬 기록")]),
                ("기기 권한", [p("사진/미디어 권한은 사용자가 사진을 가져오거나 완성한 이미지를 사진 보관함에 저장할 때 사용됩니다. 알림 권한은 사용자가 데일리 알림을 켤 때만 요청됩니다."), p("권한을 허용하지 않아도 해당 기능을 제외한 앱 기능은 계속 사용할 수 있습니다. 권한은 iOS 또는 Android의 시스템 설정에서 변경할 수 있습니다.")]),
                ("네트워크 통신 및 제3자 서비스", [p("출시 빌드의 설정에 따라 아래 서비스와 통신할 수 있습니다."), ul("Apple App Store 또는 Google Play: 인앱 구매 결제, 영수증 및 구독 상태 처리", "RevenueCat: 구매가 활성화된 빌드에서 구매 권한·복원 상태를 확인하기 위한 결제/구독 관리", "정적 콘텐츠 호스팅/CDN: 스티커팩·카탈로그 등 앱 콘텐츠를 원격으로 제공하는 경우 일반적인 HTTP 요청 정보(IP 주소, 기기/브라우저 또는 앱 요청 정보, 요청 시각 등)가 호스팅 인프라에서 처리될 수 있음"), p("Adelie Draw는 결제 카드 번호를 직접 수집하거나 저장하지 않습니다. 결제는 Apple 또는 Google의 결제 시스템을 통해 처리됩니다."), note("RevenueCat이나 앱 스토어 등 제3자 서비스가 처리하는 정보에는 해당 서비스의 개인정보처리방침과 플랫폼 정책도 적용됩니다.")]),
                ("광고·분석·추적", [p("현재 확인된 Adelie Pages 빌드에는 광고 SDK, 제3자 행동 분석 SDK 또는 앱 간 광고 추적 기능이 포함되어 있지 않습니다. Adelie Draw는 현재 앱 사용 데이터를 광고 프로파일링 목적으로 판매하지 않습니다.")]),
                ("데이터 공유", [p("Adelie Draw는 사용자가 시스템 공유 기능 또는 Instagram Stories 공유 기능을 직접 실행한 경우에만 사용자가 선택한 결과 파일을 해당 공유 대상으로 전달합니다. 공유 이후의 처리는 사용자가 선택한 앱 또는 서비스의 정책에 따릅니다."), p("구매 기능을 사용할 때는 결제·구독 상태 처리를 위해 Apple, Google, RevenueCat과 필요한 범위의 구매 관련 정보가 처리될 수 있습니다.")]),
                ("보관 및 삭제", [p("로컬 페이지·초안·가져온 사진의 앱 전용 사본은 사용자가 앱에서 삭제하거나 앱을 제거하여 로컬 앱 데이터가 삭제될 때까지 기기에 남을 수 있습니다. 사진 보관함으로 내보낸 이미지는 앱 삭제와 별개이므로 사용자가 사진 앱에서 직접 삭제해야 합니다."), p("구매 내역·구독 기록처럼 Apple, Google 또는 RevenueCat이 보관하는 데이터는 각 서비스의 보관 정책 및 적용 법령에 따라 처리될 수 있습니다."), p("현재 Adelie 계정이 없으므로 서버 계정 삭제 요청 절차는 적용되지 않습니다. 로컬 데이터 관리 방법은 데이터 및 계정 페이지에서 확인할 수 있습니다.")]),
                ("변경 및 문의", [p("앱 기능이나 데이터 처리 방식이 변경되면 이 방침도 갱신하고 시행일을 표시합니다. 개인정보 또는 데이터 처리에 관한 문의는 아래 연락처로 보낼 수 있습니다.")]),
            ],
        },
        "en": {
            "title": "Privacy Policy",
            "display": "Privacy\nPolicy",
            "summary": "This policy explains what Adelie Pages keeps on your device and what external services may process data when you use photos, notifications, purchases, or remote app content.",
            "sections": [
                ("Scope", [p("This policy applies to the Adelie Pages mobile app for iOS and Android, provided by Adelie Draw. The current release does not provide an Adelie account sign-up or sign-in feature.")]),
                ("Data processed on your device", [p("Pages, drafts, templates, journal records, favorites or recent-use information, notification preferences, and app-owned copies of photos you import may be stored locally on your device."), p("Using save or edit features does not by itself upload this content to an Adelie Draw server. The current build does not provide Adelie account-based cloud backup."), ul("Pages, drafts, text, and layout information you create", "App-owned copies of photos you choose from your photo library", "Notification preference, reminder time, time zone, and related settings", "Exported files and local activity records created by the app")]),
                ("Device permissions", [p("Photo or media access is used when you choose a photo to import or save a finished image to your photo library. Notification permission is requested only if you enable daily reminders."), p("You can continue using the rest of the app without granting these permissions. You can change permissions in iOS or Android system settings.")]),
                ("Network communications and third-party services", [p("Depending on the configuration of a release build, Adelie Pages may communicate with the following services."), ul("Apple App Store or Google Play for in-app purchase payment, receipts, and subscription status", "RevenueCat, when live purchasing is enabled, to manage and restore purchase entitlements", "Static content hosting/CDN when sticker packs or catalog content are delivered remotely; hosting infrastructure may process ordinary HTTP request information such as IP address, request/device information, and timestamps"), p("Adelie Draw does not directly collect or store your payment card number. Payments are processed through Apple or Google billing systems."), note("Information processed by third-party services such as RevenueCat or the app stores is also subject to those providers' privacy policies and platform terms.")]),
                ("Advertising, analytics, and tracking", [p("The current verified Adelie Pages build does not include an advertising SDK, third-party behavioral analytics SDK, or cross-app advertising tracking. Adelie Draw does not currently sell app usage data for advertising profiling.")]),
                ("Sharing", [p("When you explicitly use the system share sheet or Instagram Stories sharing, the output file you selected is passed to the destination you choose. Processing after that point is governed by the destination app or service."), p("If you use purchasing features, purchase-related information required to process or restore entitlements may be handled by Apple, Google, and RevenueCat.")]),
                ("Retention and deletion", [p("Local pages, drafts, and app-owned copies of imported photos may remain on your device until you delete them in the app or remove the app and its local app data. Images exported to your photo library are separate from app data and must be deleted from your photo library by you."), p("Purchase or subscription records retained by Apple, Google, or RevenueCat may be processed under each provider's retention policy and applicable law."), p("Because the current app has no Adelie account, there is no server account to delete. See the Data & Account page for local data controls.")]),
                ("Changes and contact", [p("We will update this policy when app features or data handling change and will show the effective date. Questions about privacy or data handling can be sent to the contact information below.")]),
            ],
        },
        "ja": {
            "title": "プライバシーポリシー",
            "display": "プライバシー\nポリシー",
            "summary": "Adelie Pages が端末内で扱うデータと、写真・通知・購入・リモートコンテンツの利用時に外部サービスで処理される可能性がある情報を説明します。",
            "sections": [
                ("適用範囲", [p("本ポリシーは Adelie Draw が提供する iOS・Android 向け Adelie Pages に適用されます。現在のリリースには Adelie アカウントの作成・ログイン機能はありません。")]),
                ("端末内で処理されるデータ", [p("ページ、下書き、テンプレート、ダイアリー記録、お気に入り・最近の利用情報、通知設定、取り込んだ写真のアプリ専用コピーは端末内に保存される場合があります。"), p("保存・編集機能を使っただけで、これらの内容が Adelie Draw のサーバーへアップロードされることはありません。現在のビルドには Adelie アカウントを使ったクラウドバックアップはありません。"), ul("作成したページ・下書き・テキスト・レイアウト情報", "写真ライブラリから選択した写真のアプリ専用コピー", "通知のオン/オフ、時刻、タイムゾーンなどの設定", "書き出したファイルとアプリ内のローカル記録")]),
                ("端末の権限", [p("写真/メディアへのアクセスは、写真を取り込む場合や完成画像を写真ライブラリへ保存する場合に使用します。通知権限はデイリー通知を有効にした場合のみ要求します。"), p("これらの権限を許可しなくても、それ以外の機能は利用できます。権限は iOS または Android のシステム設定から変更できます。")]),
                ("ネットワーク通信と第三者サービス", [p("リリースビルドの設定により、以下のサービスと通信する場合があります。"), ul("Apple App Store または Google Play：アプリ内購入、レシート、サブスクリプション状態の処理", "RevenueCat：購入機能が有効なビルドで購入権限や復元状態を管理", "静的コンテンツ配信/CDN：ステッカーパックやカタログをリモート配信する場合、IP アドレス、リクエスト/端末情報、時刻など通常の HTTP リクエスト情報をホスティング基盤が処理する場合があります"), p("Adelie Draw が決済カード番号を直接収集・保存することはありません。決済は Apple または Google の決済システムで処理されます。"), note("RevenueCat や各アプリストアなど第三者が処理する情報には、それぞれのプライバシーポリシーとプラットフォーム規約も適用されます。")]),
                ("広告・分析・トラッキング", [p("現在確認済みの Adelie Pages ビルドには、広告 SDK、第三者の行動分析 SDK、アプリ横断型の広告トラッキング機能は含まれていません。Adelie Draw は現在、アプリ利用データを広告プロファイリング目的で販売していません。")]),
                ("共有", [p("システム共有または Instagram Stories 共有を利用者が明示的に実行した場合、選択した出力ファイルが指定先へ渡されます。その後の処理には共有先アプリ・サービスの方針が適用されます。"), p("購入機能を利用した場合、購入権限の処理・復元に必要な購入関連情報が Apple、Google、RevenueCat で処理されることがあります。")]),
                ("保存期間と削除", [p("ローカルのページ、下書き、取り込んだ写真のアプリ専用コピーは、アプリ内で削除するか、アプリとそのローカルデータを削除するまで端末に残る場合があります。写真ライブラリへ書き出した画像はアプリデータとは別のため、写真アプリから削除してください。"), p("Apple、Google、RevenueCat が保持する購入・サブスクリプション記録は、各社の保持方針および適用法令に従って処理される場合があります。"), p("現在は Adelie アカウントがないため、サーバーアカウントの削除手続きはありません。ローカルデータの管理方法は「データとアカウント」ページをご覧ください。")]),
                ("変更とお問い合わせ", [p("アプリの機能やデータ処理方法が変わる場合は本ポリシーを更新し、施行日を表示します。プライバシーやデータ処理に関するお問い合わせは下記連絡先までお送りください。")]),
            ],
        },
        "zh": {
            "title": "隐私政策",
            "display": "隐私\n政策",
            "summary": "本政策说明 Adelie Pages 在设备本地处理哪些数据，以及在使用照片、通知、购买或远程内容时，哪些外部服务可能参与数据处理。",
            "sections": [
                ("适用范围", [p("本政策适用于 Adelie Draw 提供的 iOS 和 Android 版 Adelie Pages。当前版本不提供 Adelie 账户注册或登录功能。")]),
                ("在设备本地处理的数据", [p("页面、草稿、模板、日记记录、收藏或最近使用信息、通知设置，以及导入照片的应用专用副本可能保存在您的设备本地。"), p("仅使用保存或编辑功能不会将这些内容上传至 Adelie Draw 服务器。当前版本不提供基于 Adelie 账户的云端备份。"), ul("您创建的页面、草稿、文字和布局信息", "您从照片库选择的照片之应用专用副本", "通知开关、提醒时间、时区等设置", "应用创建的导出文件和本地记录")]),
                ("设备权限", [p("照片/媒体权限仅在您导入照片或将完成的图片保存到照片库时使用。通知权限仅在您开启每日提醒时请求。"), p("拒绝这些权限后，除相应功能外，应用的其他功能仍可使用。您可以在 iOS 或 Android 系统设置中更改权限。")]),
                ("网络通信与第三方服务", [p("根据发布版本的配置，Adelie Pages 可能与以下服务通信。"), ul("Apple App Store 或 Google Play：处理应用内购买、收据和订阅状态", "RevenueCat：在启用正式购买功能时管理及恢复购买权益", "静态内容托管/CDN：远程提供贴纸包或目录内容时，托管基础设施可能处理常规 HTTP 请求信息，例如 IP 地址、请求/设备信息和时间戳"), p("Adelie Draw 不直接收集或保存您的支付卡号。付款通过 Apple 或 Google 的支付系统处理。"), note("RevenueCat、应用商店等第三方服务处理的信息同时受其自身隐私政策和平台条款约束。")]),
                ("广告、分析与跟踪", [p("当前已核验的 Adelie Pages 版本不包含广告 SDK、第三方行为分析 SDK 或跨应用广告跟踪功能。Adelie Draw 目前不会出售应用使用数据用于广告画像。")]),
                ("共享", [p("只有当您主动使用系统分享或 Instagram Stories 分享时，您选择的输出文件才会传递给您指定的目标。之后的数据处理受目标应用或服务的政策约束。"), p("使用购买功能时，为处理或恢复购买权益所需的购买相关信息可能由 Apple、Google 和 RevenueCat 处理。")]),
                ("保留与删除", [p("本地页面、草稿和导入照片的应用专用副本可能保留在设备上，直到您在应用中删除它们，或删除应用及其本地数据。已经导出到照片库的图片独立于应用数据，需要您在照片应用中自行删除。"), p("Apple、Google 或 RevenueCat 保存的购买或订阅记录，可能依据各服务的保留政策和适用法律处理。"), p("由于当前应用没有 Adelie 账户，因此不存在需要删除的服务器账户。有关本地数据控制，请参阅“数据与账户”页面。")]),
                ("变更与联系", [p("如果应用功能或数据处理方式发生变化，我们会更新本政策并标示生效日期。有关隐私或数据处理的问题，可通过下方联系方式与我们联系。")]),
            ],
        },
    },
    "support": {
        "ko": {
            "title": "Adelie Pages 지원",
            "display": "지원\n센터",
            "summary": "앱 사용 중 발생한 문제, 구매 복원, 사진·저장·알림 권한, 데이터 처리 문의를 받을 수 있는 공식 지원 페이지입니다.",
            "sections": [
                ("문의하기", [p("지원 요청에는 사용 중인 기기와 OS 버전, Adelie Pages 버전, 문제가 발생한 화면, 재현 순서를 함께 적어 주면 확인에 도움이 됩니다. 필요한 경우 스크린샷을 첨부할 수 있습니다."), p("계정 비밀번호나 결제 카드 전체 번호와 같은 민감한 인증정보는 지원 메일에 포함하지 마세요.")]),
                ("사진 불러오기·저장", [p("사진 불러오기가 되지 않으면 시스템 설정에서 Adelie Pages의 사진 접근 권한을 확인하세요. 완성 이미지를 사진 보관함에 저장하는 기능도 사진/미디어 저장 권한이 필요할 수 있습니다."), p("가져온 사진은 편집을 위해 앱 전용 로컬 저장소에 복사될 수 있습니다.")]),
                ("페이지·초안 보관", [p("현재 페이지, 초안, 템플릿은 기기에 로컬로 저장되며 Adelie 계정 기반 클라우드 백업은 제공되지 않습니다. 앱 재설치 또는 기기 분실 시 로컬 작업물이 사라질 수 있으므로 중요한 결과물은 이미지로 내보내 보관하세요."), p("페이지를 삭제한 직후 실행 취소가 표시되는 경우에만 즉시 복구할 수 있습니다.")]),
                ("구매 및 복원", [p("구매 기능이 활성화된 빌드에서는 결제가 Apple App Store 또는 Google Play를 통해 처리됩니다. 같은 스토어 계정으로 설치한 뒤 앱의 구매 복원 기능을 사용할 수 있습니다."), p("결제 취소·환불·구독 관리는 구매한 스토어의 정책과 계정 관리 화면을 따릅니다. Adelie Draw는 결제 카드 번호를 직접 보관하지 않습니다.")]),
                ("알림", [p("데일리 알림을 켰는데 알림이 오지 않으면 시스템 알림 권한, 앱에서 선택한 알림 시각과 시간대를 확인하세요. Adelie Pages의 현재 알림은 기기에서 예약되는 로컬 알림입니다.")]),
                ("개인정보·데이터", [p("개인정보 처리 방식은 개인정보처리방침을, 로컬 데이터 삭제와 권한 관리 방법은 데이터 및 계정 페이지를 확인하세요.")]),
            ],
        },
        "en": {
            "title": "Adelie Pages Support",
            "display": "Support\nCenter",
            "summary": "Official support for app issues, purchase restoration, photo/save/notification permissions, and questions about data handling.",
            "sections": [
                ("Contact support", [p("When reporting an issue, include your device and OS version, Adelie Pages version, the screen where the issue occurred, and steps to reproduce it. You may attach a screenshot if useful."), p("Do not include sensitive authentication information such as account passwords or full payment card numbers in support email.")]),
                ("Importing and saving photos", [p("If photo import does not work, check Adelie Pages photo access in system settings. Saving finished images to the photo library may also require photo or media write access."), p("A photo you import may be copied into app-owned local storage so the page can be edited later.")]),
                ("Pages and drafts", [p("Pages, drafts, and templates are currently stored locally on the device. Adelie account-based cloud backup is not available. Reinstalling the app or losing the device may remove local work, so export important pages as images."), p("A deleted page can only be restored immediately when an Undo option is shown.")]),
                ("Purchases and restore", [p("When purchasing is enabled, transactions are processed through the Apple App Store or Google Play. After reinstalling with the same store account, use the in-app restore purchases function when available."), p("Cancellation, refunds, and subscription management follow the store where you purchased. Adelie Draw does not directly store payment card numbers.")]),
                ("Notifications", [p("If daily reminders are enabled but not arriving, check system notification permission, reminder time, and time zone in the app. Current Adelie Pages reminders are scheduled locally on the device.")]),
                ("Privacy and data", [p("See the Privacy Policy for data handling and the Data & Account page for local data deletion and permission controls.")]),
            ],
        },
        "ja": {
            "title": "Adelie Pages サポート",
            "display": "サポート\nセンター",
            "summary": "アプリの不具合、購入の復元、写真・保存・通知の権限、データ処理に関するお問い合わせの公式窓口です。",
            "sections": [
                ("お問い合わせ", [p("不具合を報告する際は、端末と OS のバージョン、Adelie Pages のバージョン、問題が発生した画面、再現手順をご記載ください。必要に応じてスクリーンショットも添付できます。"), p("アカウントのパスワードや決済カード番号全体など、機密性の高い認証情報はメールに記載しないでください。")]),
                ("写真の取り込み・保存", [p("写真を取り込めない場合は、システム設定で Adelie Pages の写真アクセス権限をご確認ください。完成画像を写真ライブラリへ保存する場合も写真/メディアの保存権限が必要になることがあります。"), p("取り込んだ写真は後から編集できるよう、アプリ専用のローカル領域へコピーされる場合があります。")]),
                ("ページ・下書きの保存", [p("現在、ページ・下書き・テンプレートは端末内に保存され、Adelie アカウントを使ったクラウドバックアップはありません。再インストールや端末紛失でローカルデータが失われる場合があるため、大切なページは画像として書き出してください。"), p("削除直後に「取り消し」が表示された場合のみ、その場で復元できます。")]),
                ("購入と復元", [p("購入機能が有効なビルドでは、決済は Apple App Store または Google Play を通じて処理されます。同じストアアカウントで再インストールした場合は、アプリ内の購入復元機能をご利用ください。"), p("キャンセル、返金、サブスクリプション管理は購入したストアのポリシーとアカウント画面に従います。Adelie Draw は決済カード番号を直接保存しません。")]),
                ("通知", [p("デイリー通知を有効にしても届かない場合は、システムの通知権限、アプリで設定した通知時刻、タイムゾーンをご確認ください。現在の Adelie Pages の通知は端末上で予約されるローカル通知です。")]),
                ("プライバシーとデータ", [p("データ処理についてはプライバシーポリシー、ローカルデータの削除や権限管理については「データとアカウント」ページをご覧ください。")]),
            ],
        },
        "zh": {
            "title": "Adelie Pages 支持",
            "display": "支持\n中心",
            "summary": "用于联系 Adelie Pages 官方支持，处理应用问题、恢复购买、照片/保存/通知权限及数据处理相关问题。",
            "sections": [
                ("联系支持", [p("提交问题时，请提供设备与系统版本、Adelie Pages 版本、发生问题的页面以及复现步骤。如有帮助，也可以附上截图。"), p("请勿在支持邮件中发送账户密码或完整支付卡号等敏感认证信息。")]),
                ("导入与保存照片", [p("如果无法导入照片，请在系统设置中检查 Adelie Pages 的照片访问权限。将完成的图片保存到照片库时，也可能需要照片或媒体写入权限。"), p("为了以后继续编辑，您导入的照片可能会复制到应用专用的本地存储中。")]),
                ("页面与草稿", [p("当前页面、草稿和模板保存在设备本地，不提供基于 Adelie 账户的云端备份。重新安装应用或设备丢失可能导致本地作品丢失，请将重要页面导出为图片保存。"), p("页面删除后，只有在立即出现“撤销”选项时才能当场恢复。")]),
                ("购买与恢复", [p("启用购买功能的版本通过 Apple App Store 或 Google Play 处理交易。使用同一商店账户重新安装后，可使用应用内的恢复购买功能。"), p("取消、退款和订阅管理遵循您购买时所用商店的规则与账户管理页面。Adelie Draw 不直接保存支付卡号。")]),
                ("通知", [p("如果已开启每日提醒但未收到通知，请检查系统通知权限、应用内提醒时间和时区。当前 Adelie Pages 的提醒是在设备本地安排的通知。")]),
                ("隐私与数据", [p("数据处理方式请参阅《隐私政策》；本地数据删除和权限管理请参阅“数据与账户”页面。")]),
            ],
        },
    },
    "terms": {
        "ko": {
            "title": "Adelie Pages 이용약관",
            "display": "이용\n약관",
            "summary": "Adelie Pages 앱, 제공 콘텐츠, 인앱 구매 및 결과물 사용에 적용되는 기본 이용 조건입니다.",
            "sections": [
                ("약관의 적용", [p("이 약관은 Adelie Draw가 제공하는 Adelie Pages 앱과 앱을 통해 제공되는 디지털 콘텐츠의 이용에 적용됩니다. 앱을 설치하거나 이용하면 이 약관과 적용되는 Apple App Store 또는 Google Play의 플랫폼 조건이 함께 적용될 수 있습니다.")]),
                ("앱 이용 권한", [p("Adelie Draw는 사용자가 개인 기기에서 Adelie Pages를 이용할 수 있도록 비독점적이고 양도할 수 없는 제한적 이용 권한을 부여합니다. 앱 또는 포함된 자산의 소유권 자체가 사용자에게 이전되는 것은 아닙니다.")]),
                ("사용자가 만든 콘텐츠", [p("사용자가 직접 입력한 텍스트, 불러온 사진 등 사용자 소유 콘텐츠에 대한 권리는 사용자에게 남습니다. 사용자는 앱에서 페이지를 만들고 기기에 저장하거나 지원되는 공유 기능으로 내보낼 수 있습니다."), p("사용자는 자신이 불러오거나 공유하는 콘텐츠를 사용할 권한이 있는지 스스로 확인해야 합니다.")]),
                ("Adelie Draw 제공 자산", [p("앱에서 제공되는 스티커, 일러스트, 템플릿, 브랜드 요소 등은 Adelie Draw 또는 해당 권리자의 자산입니다. 앱은 이러한 자산을 Adelie Pages에서 페이지를 만들고 허용된 방식으로 결과물을 내보내는 데 사용할 수 있는 범위의 이용 권한을 제공합니다."), p("개별 원본 자산을 별도 파일로 추출·재배포·재판매할 권리는 명시적으로 허용된 경우를 제외하고 부여되지 않습니다. 팩별 별도 이용 조건이 표시되는 경우 해당 조건이 우선 적용됩니다.")]),
                ("인앱 구매 및 구독", [p("유료 팩, 기능 또는 구독이 제공되는 경우 결제는 Apple App Store 또는 Google Play를 통해 처리될 수 있습니다. 가격, 결제 주기, 자동 갱신 여부와 구독 혜택은 구매 화면에 표시됩니다."), p("자동 갱신 구독은 사용자가 스토어 계정 설정에서 취소하지 않는 한 스토어 정책에 따라 갱신될 수 있습니다. 취소·환불·청구 관리는 구매한 스토어의 정책을 따릅니다. 앱은 지원되는 경우 구매 복원 기능을 제공합니다."), note("iOS에서 별도의 맞춤형 EULA가 App Store Connect에 등록되지 않은 경우 Apple의 표준 EULA도 적용될 수 있습니다.")]),
                ("서비스 변경", [p("Adelie Draw는 앱 기능, 무료/유료 콘텐츠 구성, 지원 플랫폼 또는 원격 카탈로그를 업데이트할 수 있습니다. 이미 완료된 유료 구매의 권리는 해당 구매 조건과 스토어 정책에 따라 처리됩니다.")]),
                ("이용 제한", [p("관련 법령을 위반하거나, 앱·서비스의 정상 동작을 방해하거나, 권한 없이 앱 자산을 복제·재배포하기 위해 기술적 보호조치를 우회하는 방식으로 앱을 이용해서는 안 됩니다.")]),
                ("보증 및 책임", [p("앱은 적용 법령이 허용하는 범위에서 제공됩니다. Adelie Draw는 사용자가 만든 로컬 데이터의 영구 보존을 보장하지 않으며, 현재 빌드에는 계정 기반 클라우드 백업이 없습니다. 중요한 결과물은 별도로 내보내 보관하는 것이 필요합니다."), p("법령상 배제할 수 없는 소비자 권리와 책임은 이 약관으로 제한되지 않습니다.")]),
                ("준거법 및 문의", [p("이 약관은 적용되는 강행 소비자보호 규정을 제외하고 대한민국 법령을 기준으로 해석합니다. 약관 또는 앱 이용에 관한 문의는 아래 연락처로 보낼 수 있습니다.")]),
            ],
        },
        "en": {
            "title": "Adelie Pages Terms of Use",
            "display": "Terms of\nUse",
            "summary": "Basic terms that apply to the Adelie Pages app, app-provided assets, in-app purchases, subscriptions, and exported creations.",
            "sections": [
                ("Application of these terms", [p("These terms apply to the Adelie Pages app and digital content provided by Adelie Draw. When you install or use the app, applicable Apple App Store or Google Play platform terms may also apply.")]),
                ("License to use the app", [p("Adelie Draw grants you a limited, non-exclusive, non-transferable right to use Adelie Pages on your personal device. Ownership of the app and its included assets is not transferred to you.")]),
                ("Your content", [p("You retain rights in content you provide, such as text you enter and photos you import. You may use Adelie Pages to create pages, store them on your device, and export them through supported sharing functions."), p("You are responsible for having the rights needed to use content you import or share.")]),
                ("Adelie Draw assets", [p("Stickers, illustrations, templates, brand elements, and other app-provided assets are owned by Adelie Draw or the applicable rights holder. The app licenses them for use in creating pages in Adelie Pages and exporting resulting pages in supported ways."), p("No right to extract, redistribute, or resell individual source assets as standalone files is granted unless expressly permitted. If a pack shows separate usage terms, those pack-specific terms control for that pack.")]),
                ("In-app purchases and subscriptions", [p("If paid packs, features, or subscriptions are offered, payment may be processed through the Apple App Store or Google Play. Price, billing period, auto-renewal status, and subscription benefits are shown in the purchase flow."), p("Auto-renewing subscriptions may renew under the store's rules unless you cancel them in your store account settings. Cancellation, refunds, and billing management follow the store where the purchase was made. Restore purchases is provided where supported."), note("On iOS, Apple's Standard EULA may also apply when no separate custom EULA is supplied in App Store Connect.")]),
                ("Changes to the service", [p("Adelie Draw may update app features, the mix of free and paid content, supported platforms, or remote catalog content. Rights from completed paid purchases are handled under the terms of that purchase and applicable store rules.")]),
                ("Restrictions", [p("You may not use the app to violate applicable law, interfere with normal operation of the app or service, or bypass technical protections to make unauthorized copies or redistribution of app assets.")]),
                ("Warranty and liability", [p("The app is provided subject to applicable law. Adelie Draw does not guarantee permanent retention of local user data, and the current build does not provide account-based cloud backup. Important outputs should be exported separately."), p("Nothing in these terms limits consumer rights or liabilities that cannot legally be excluded.")]),
                ("Governing law and contact", [p("These terms are interpreted under the laws of the Republic of Korea, subject to mandatory consumer protection rules that apply in your jurisdiction. Questions about these terms or app use can be sent to the contact information below.")]),
            ],
        },
        "ja": {
            "title": "Adelie Pages 利用規約",
            "display": "利用\n規約",
            "summary": "Adelie Pages、アプリ内の素材、アプリ内購入・サブスクリプション、書き出した作品に適用される基本条件です。",
            "sections": [
                ("本規約の適用", [p("本規約は Adelie Draw が提供する Adelie Pages とデジタルコンテンツに適用されます。アプリのインストール・利用には、適用される Apple App Store または Google Play のプラットフォーム条件も適用される場合があります。")]),
                ("アプリの利用許諾", [p("Adelie Draw は、個人端末で Adelie Pages を利用するための限定的、非独占的、譲渡不可の利用権を付与します。アプリまたは同梱素材の所有権が利用者へ移転するものではありません。")]),
                ("利用者のコンテンツ", [p("利用者が入力したテキストや取り込んだ写真など、利用者が提供するコンテンツの権利は利用者に残ります。Adelie Pages でページを作成し、端末へ保存し、対応する共有機能で書き出すことができます。"), p("取り込み・共有するコンテンツを利用するために必要な権利を有していることは利用者の責任です。")]),
                ("Adelie Draw の素材", [p("ステッカー、イラスト、テンプレート、ブランド要素などのアプリ内素材は Adelie Draw または各権利者に帰属します。Adelie Pages でページを作成し、対応する方法で完成ページを書き出す範囲で利用できます。"), p("明示的に許可されている場合を除き、個別の元素材を単体ファイルとして抽出・再配布・再販売する権利は付与されません。パックごとに別の利用条件が表示される場合は、その条件が当該パックに優先して適用されます。")]),
                ("アプリ内購入とサブスクリプション", [p("有料パック、機能、サブスクリプションを提供する場合、決済は Apple App Store または Google Play を通じて処理されます。価格、請求期間、自動更新の有無、特典は購入画面に表示されます。"), p("自動更新サブスクリプションは、ストアアカウント設定で解約しない限りストアの規則に従って更新される場合があります。解約・返金・請求管理は購入したストアの規則に従います。対応する場合は購入の復元機能を提供します。"), note("iOS では App Store Connect に独自 EULA を登録していない場合、Apple の標準 EULA も適用されることがあります。")]),
                ("サービスの変更", [p("Adelie Draw は、アプリ機能、無料/有料コンテンツの構成、対応プラットフォーム、リモートカタログを更新することがあります。完了済みの有料購入に基づく権利は、購入条件とストア規則に従って扱われます。")]),
                ("利用制限", [p("適用法令に違反する目的、アプリやサービスの正常な動作を妨げる目的、または技術的保護を回避してアプリ素材を無断で複製・再配布する目的で利用してはなりません。")]),
                ("保証と責任", [p("アプリは適用法令の範囲で提供されます。Adelie Draw はローカルデータの永久保存を保証せず、現在のビルドにはアカウント型クラウドバックアップがありません。重要な成果物は別途書き出して保管してください。"), p("法令上排除できない消費者の権利や責任は、本規約によって制限されません。")]),
                ("準拠法とお問い合わせ", [p("本規約は、各地域で適用される強行的な消費者保護規定を除き、大韓民国の法令に基づいて解釈されます。本規約またはアプリ利用に関するお問い合わせは下記連絡先までお送りください。")]),
            ],
        },
        "zh": {
            "title": "Adelie Pages 使用条款",
            "display": "使用\n条款",
            "summary": "适用于 Adelie Pages 应用、应用内素材、应用内购买与订阅以及导出作品的基本使用条件。",
            "sections": [
                ("条款适用", [p("本条款适用于 Adelie Draw 提供的 Adelie Pages 及其数字内容。安装或使用本应用时，适用的 Apple App Store 或 Google Play 平台条款也可能同时适用。")]),
                ("应用使用许可", [p("Adelie Draw 授予您在个人设备上使用 Adelie Pages 的有限、非独占、不可转让许可。应用及其中素材的所有权不会因此转移给您。")]),
                ("您的内容", [p("您对自己提供的内容保留相应权利，例如您输入的文字和导入的照片。您可以使用 Adelie Pages 创建页面、将其保存在设备上，并通过支持的分享功能导出。"), p("您有责任确保自己拥有使用所导入或分享内容所需的权利。")]),
                ("Adelie Draw 提供的素材", [p("贴纸、插画、模板、品牌元素及其他应用内素材归 Adelie Draw 或相应权利人所有。应用授予的许可仅用于在 Adelie Pages 中制作页面并以支持的方式导出成品页面。"), p("除非明确许可，您无权将单个原始素材作为独立文件提取、再分发或转售。如果某个素材包显示单独的使用条件，则该素材包以其专用条件为准。")]),
                ("应用内购买与订阅", [p("如提供付费素材包、功能或订阅，付款可通过 Apple App Store 或 Google Play 处理。价格、计费周期、是否自动续订以及订阅权益会在购买流程中显示。"), p("自动续订订阅可能会按照商店规则续订，除非您在商店账户设置中取消。取消、退款和账单管理遵循购买所在商店的规则。支持时，应用会提供恢复购买功能。"), note("在 iOS 上，如果 App Store Connect 中未提供单独的自定义 EULA，Apple 标准 EULA 也可能适用。")]),
                ("服务变更", [p("Adelie Draw 可能更新应用功能、免费/付费内容构成、支持平台或远程目录内容。已完成的付费购买所产生的权利，按照购买条件及适用商店规则处理。")]),
                ("使用限制", [p("不得使用本应用违反适用法律、干扰应用或服务正常运行，或绕过技术保护措施以未经授权复制、再分发应用素材。")]),
                ("保证与责任", [p("本应用在适用法律允许的范围内提供。Adelie Draw 不保证本地用户数据永久保存，当前版本也不提供基于账户的云端备份。重要成品应另行导出保存。"), p("本条款不会限制法律上不可排除的消费者权利或责任。")]),
                ("适用法律与联系", [p("除您所在地区强制适用的消费者保护规定外，本条款按韩国法律解释。有关条款或应用使用的问题，可通过下方联系方式联系我们。")]),
            ],
        },
    },
    "data": {
        "ko": {
            "title": "데이터 및 계정 관리",
            "display": "데이터 및\n계정 관리",
            "summary": "현재 Adelie Pages는 Adelie 계정을 만들지 않습니다. 이 페이지는 로컬 데이터 삭제, 권한 해제, 구매·구독 관리 방법을 안내합니다.",
            "sections": [
                ("현재 계정 상태", [p("현재 Adelie Pages에는 Adelie 계정 가입이나 로그인이 없습니다. 따라서 Adelie Draw 서버에 삭제할 사용자 계정도 없습니다."), note("Google Play의 외부 계정 삭제 URL 요구사항은 앱이 계정 생성을 제공할 때 적용됩니다. 계정 기능이 추가되면 이 페이지를 실제 계정 삭제 요청 경로로 갱신합니다.")]),
                ("페이지와 초안 삭제", [p("페이지·초안·템플릿은 현재 기기에 로컬로 저장됩니다. 앱 안에서 개별 항목을 삭제할 수 있으며, 삭제 직후 실행 취소가 표시될 때만 즉시 복구할 수 있습니다."), p("앱을 제거하면서 앱의 로컬 데이터도 함께 삭제하면 앱 전용 저장소의 페이지·초안·가져온 사진 사본 등이 제거될 수 있습니다. 기기 백업이나 운영체제의 복원 기능이 별도로 동작하는 경우에는 해당 플랫폼 설정을 확인해야 합니다.")]),
                ("사진 보관함의 내보낸 이미지", [p("Adelie Pages에서 사진 보관함으로 저장한 PNG 등 결과 이미지는 앱 로컬 데이터와 별개입니다. 앱을 삭제해도 사진 보관함에 남을 수 있으며, 삭제하려면 사진 앱에서 직접 제거하세요.")]),
                ("사진·알림 권한 해제", [p("iOS 또는 Android의 시스템 설정에서 Adelie Pages의 사진/미디어 및 알림 권한을 변경하거나 해제할 수 있습니다. 알림은 앱 설정에서도 끌 수 있습니다.")]),
                ("구매와 구독", [p("앱 스토어 결제 내역과 구독은 Apple 또는 Google 계정에 연결됩니다. 앱 삭제는 구독 취소가 아닙니다. 구독이 제공되는 경우 App Store 또는 Google Play의 구독 관리 화면에서 취소·관리해야 합니다."), p("구매 관련 데이터의 열람·삭제 가능 범위는 각 스토어와 RevenueCat의 정책 및 법적 보관 의무에 따를 수 있습니다.")]),
                ("데이터 문의", [p("Adelie Draw가 처리하는 데이터에 관한 질문이나 지원이 필요하면 아래 이메일로 문의하세요. 현재 계정이 없기 때문에 이메일을 보내는 것만으로 앱 로컬 데이터를 원격 삭제할 수는 없습니다.")]),
            ],
        },
        "en": {
            "title": "Data & Account Management",
            "display": "Data &\nAccount",
            "summary": "Adelie Pages currently does not create an Adelie account. This page explains local data deletion, permission controls, and purchase or subscription management.",
            "sections": [
                ("Current account status", [p("Adelie Pages currently has no Adelie account sign-up or sign-in. There is therefore no Adelie Draw server account associated with you that can be deleted."), note("Google Play's external account deletion URL requirement applies when an app offers account creation. If account functionality is added, this page will be updated to provide the actual account deletion request path.")]),
                ("Delete pages and drafts", [p("Pages, drafts, and templates are currently stored locally on your device. You can delete individual items in the app; immediate recovery is only available when an Undo option appears right after deletion."), p("Removing the app together with its local app data may delete pages, drafts, and app-owned copies of imported photos. If your operating system or device backup restores app data separately, review the relevant platform backup settings.")]),
                ("Images exported to your photo library", [p("PNG or other result images saved from Adelie Pages to your photo library are separate from the app's local data. They may remain after the app is deleted and must be removed from your photo library by you.")]),
                ("Revoke photo and notification permissions", [p("You can change or revoke Adelie Pages photo/media and notification permissions in iOS or Android system settings. Notifications can also be turned off in the app.")]),
                ("Purchases and subscriptions", [p("App-store purchase history and subscriptions are linked to your Apple or Google account. Deleting the app does not cancel a subscription. If subscriptions are offered, manage or cancel them in the App Store or Google Play subscription settings."), p("Access to or deletion of purchase-related records may be governed by the policies and legal retention obligations of the applicable store and RevenueCat.")]),
                ("Data questions", [p("For questions or support about data processed by Adelie Draw, contact us using the email below. Because there is currently no account, sending an email cannot remotely erase data that exists only in your app's local storage.")]),
            ],
        },
        "ja": {
            "title": "データとアカウント管理",
            "display": "データと\nアカウント",
            "summary": "現在の Adelie Pages には Adelie アカウントがありません。ローカルデータの削除、権限の解除、購入・サブスクリプションの管理方法を案内します。",
            "sections": [
                ("現在のアカウント状態", [p("現在の Adelie Pages には Adelie アカウントの登録・ログイン機能がありません。そのため Adelie Draw のサーバー上に削除対象となる利用者アカウントもありません。"), note("Google Play の外部アカウント削除 URL 要件は、アプリがアカウント作成を提供する場合に適用されます。今後アカウント機能を追加した場合は、このページを実際の削除申請手続きへ更新します。")]),
                ("ページと下書きの削除", [p("ページ、下書き、テンプレートは現在端末内に保存されます。アプリ内で個別に削除でき、削除直後に「取り消し」が表示された場合のみその場で復元できます。"), p("アプリとローカルアプリデータを削除すると、ページ、下書き、取り込んだ写真のアプリ専用コピーなどが削除される場合があります。OS や端末バックアップが別途データを復元する場合は、各プラットフォームのバックアップ設定もご確認ください。")]),
                ("写真ライブラリへ書き出した画像", [p("Adelie Pages から写真ライブラリへ保存した PNG などの完成画像はアプリのローカルデータとは別です。アプリを削除しても残ることがあるため、写真アプリから利用者自身で削除してください。")]),
                ("写真・通知権限の解除", [p("iOS または Android のシステム設定で Adelie Pages の写真/メディア権限と通知権限を変更・解除できます。通知はアプリ内設定からもオフにできます。")]),
                ("購入とサブスクリプション", [p("アプリストアの購入履歴とサブスクリプションは Apple または Google アカウントに紐づきます。アプリの削除はサブスクリプション解約にはなりません。サブスクリプションを提供している場合は App Store または Google Play の管理画面から解約・管理してください。"), p("購入関連記録の参照・削除可能範囲は、各ストアおよび RevenueCat の方針や法的保存義務に従う場合があります。")]),
                ("データに関するお問い合わせ", [p("Adelie Draw が処理するデータについてご質問やサポートが必要な場合は、下記メールアドレスまでお問い合わせください。現在アカウントがないため、メールを送るだけで端末内だけに存在するローカルデータを遠隔削除することはできません。")]),
            ],
        },
        "zh": {
            "title": "数据与账户管理",
            "display": "数据与\n账户管理",
            "summary": "Adelie Pages 当前不创建 Adelie 账户。本页说明如何删除本地数据、撤销权限，以及管理购买或订阅。",
            "sections": [
                ("当前账户状态", [p("Adelie Pages 当前没有 Adelie 账户注册或登录功能，因此 Adelie Draw 服务器上也没有与您对应、需要删除的用户账户。"), note("Google Play 的外部账户删除 URL 要求适用于提供账户创建功能的应用。如果以后加入账户功能，本页面将更新为实际的账户删除申请入口。")]),
                ("删除页面与草稿", [p("页面、草稿和模板目前保存在设备本地。您可以在应用内删除单个项目；只有在删除后立即出现“撤销”选项时，才能当场恢复。"), p("删除应用并同时删除其本地应用数据，可能会移除页面、草稿及导入照片的应用专用副本。如果操作系统或设备备份会另外恢复应用数据，请同时检查相应平台的备份设置。")]),
                ("导出到照片库的图片", [p("从 Adelie Pages 保存到照片库的 PNG 等成品图片独立于应用本地数据。删除应用后它们仍可能保留，需要您在照片应用中自行删除。")]),
                ("撤销照片与通知权限", [p("您可以在 iOS 或 Android 系统设置中更改或撤销 Adelie Pages 的照片/媒体和通知权限。通知也可在应用设置中关闭。")]),
                ("购买与订阅", [p("应用商店购买记录和订阅与您的 Apple 或 Google 账户关联。删除应用不会取消订阅。如果提供订阅，请在 App Store 或 Google Play 的订阅管理页面中取消或管理。"), p("购买相关记录的访问或删除范围可能受相应商店及 RevenueCat 的政策和法定保留义务约束。")]),
                ("数据问题", [p("如果您对 Adelie Draw 处理的数据有疑问或需要支持，请使用下方电子邮件联系我们。由于当前没有账户，仅发送邮件无法远程删除只存在于您设备本地存储中的数据。")]),
            ],
        },
    },
    "info": {
        "ko": {
            "title": "Adelie Pages 앱 정보",
            "display": "앱\n정보",
            "summary": "Adelie Pages의 운영자, 지원 플랫폼, 언어, 저장 방식과 공식 연락처를 한 곳에서 확인할 수 있습니다.",
            "sections": [
                ("Adelie Pages", [p("Adelie Pages는 Adelie Draw의 디지털 문구 앱입니다. 사진 또는 빈 종이에서 시작해 스티커와 텍스트를 배치하고, 만든 페이지를 기기에 저장해 다시 편집하거나 이미지로 내보낼 수 있습니다."), ul("플랫폼: iOS · Android", "지원 화면: phone · tablet", "앱 언어: 한국어 · English · 日本語 · 中文", "현재 저장 방식: 기기 로컬 저장", "내보내기: PNG 저장 · 시스템 공유")]),
                ("운영자", [p("Adelie Pages는 Adelie Draw(아델리드로우)가 운영합니다. 앱 사용·개인정보·스토어 제출 관련 공식 연락처는 아래와 같습니다.")]),
                ("출시 상태", [p("2026년 9월 현재 App Store 및 Google Play 공개 배포를 준비 중입니다. 스토어 링크는 출시 후 이 페이지에 추가될 수 있습니다.")]),
                ("법적 문서와 지원", [p("개인정보처리방침, 이용약관, 데이터 및 계정 관리, 지원 페이지는 이 사이트의 상단 메뉴에서 확인할 수 있습니다.")]),
            ],
        },
        "en": {
            "title": "Adelie Pages App Information",
            "display": "App\nInformation",
            "summary": "Operator details, supported platforms and languages, local storage behavior, and official contact information for Adelie Pages.",
            "sections": [
                ("Adelie Pages", [p("Adelie Pages is a digital stationery app by Adelie Draw. Start from a photo or blank paper, arrange stickers and text, keep pages locally for later editing, and export finished pages as images."), ul("Platforms: iOS · Android", "Layouts: phone · tablet", "App languages: 한국어 · English · 日本語 · 中文", "Current storage: local on-device storage", "Export: PNG save · system share")]),
                ("Operator", [p("Adelie Pages is operated by Adelie Draw. The official contact information for app support, privacy, and store-related matters is shown below.")]),
                ("Release status", [p("As of September 2026, public release on the App Store and Google Play is being prepared. Store links may be added to this page after release.")]),
                ("Legal documents and support", [p("Use the navigation above to open the Privacy Policy, Terms of Use, Data & Account page, and Support page.")]),
            ],
        },
        "ja": {
            "title": "Adelie Pages アプリ情報",
            "display": "アプリ\n情報",
            "summary": "Adelie Pages の運営者、対応プラットフォーム・言語、保存方式、公式連絡先をまとめています。",
            "sections": [
                ("Adelie Pages", [p("Adelie Pages は Adelie Draw のデジタル文具アプリです。写真や白紙から始め、ステッカーとテキストを配置し、作成したページを端末に保存して再編集したり画像として書き出したりできます。"), ul("プラットフォーム：iOS · Android", "対応画面：phone · tablet", "アプリ言語：한국어 · English · 日本語 · 中文", "現在の保存方式：端末内ローカル保存", "書き出し：PNG 保存 · システム共有")]),
                ("運営者", [p("Adelie Pages は Adelie Draw が運営しています。アプリサポート、プライバシー、ストア関連の公式連絡先は下記の通りです。")]),
                ("リリース状況", [p("2026年9月現在、App Store および Google Play での一般公開を準備中です。公開後、このページにストアリンクを追加する場合があります。")]),
                ("法的文書とサポート", [p("上部ナビゲーションからプライバシーポリシー、利用規約、データとアカウント、サポートページを確認できます。")]),
            ],
        },
        "zh": {
            "title": "Adelie Pages 应用信息",
            "display": "应用\n信息",
            "summary": "集中提供 Adelie Pages 的运营方、支持平台与语言、本地存储方式和官方联系方式。",
            "sections": [
                ("Adelie Pages", [p("Adelie Pages 是 Adelie Draw 的数字文具应用。您可以从照片或空白纸张开始，摆放贴纸与文字，将页面保存在设备上继续编辑，并把完成的页面导出为图片。"), ul("平台：iOS · Android", "支持布局：phone · tablet", "应用语言：한국어 · English · 日本語 · 中文", "当前存储方式：设备本地存储", "导出：保存 PNG · 系统分享")]),
                ("运营方", [p("Adelie Pages 由 Adelie Draw 运营。应用支持、隐私及商店相关事项的官方联系方式如下。")]),
                ("发布状态", [p("截至 2026 年 9 月，Adelie Pages 正在准备通过 App Store 和 Google Play 公开发布。发布后，本页可能会添加商店链接。")]),
                ("法律文件与支持", [p("可通过上方导航访问《隐私政策》《使用条款》、“数据与账户”以及“支持”页面。")]),
            ],
        },
    },
}


def render_item(item):
    kind, value = item
    if kind == "p":
        return f"<p>{escape(value)}</p>"
    if kind == "ul":
        return "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in value) + "</ul>"
    if kind == "note":
        return f'<div class="legal-note">{escape(value)}</div>'
    raise ValueError(kind)


def header(active, lang):
    c = COMMON[lang]
    links = ""
    for key in ("privacy", "support", "terms", "data", "info"):
        current = ' aria-current="page"' if key == active else ""
        links += f'<a href="/{key}/?lang={lang}"{current}>{escape(NAV[lang][key])}</a>'
    return f"""
  <a class="skip" href="#main-{lang}">Skip to content</a>
  <header class="legal-header">
    <div class="wrap legal-header-inner">
      <a class="legal-brand" href="/?lang={lang}" aria-label="{escape(c['home'])}">
        <img src="/assets/img/brand/app-icon.png" width="36" height="36" alt="">
        <span>Adelie Pages<small>by Adelie Draw</small></span>
      </a>
      <nav class="legal-nav" aria-label="Legal and support">{links}</nav>
    </div>
  </header>"""


def footer(lang):
    n = NAV[lang]
    return f"""
  <footer class="legal-footer">
    <div class="wrap legal-footer-inner">
      <div><strong>Adelie Pages</strong><p>© 2026 Adelie Draw</p></div>
      <nav>
        <a href="/privacy/?lang={lang}">{escape(n['privacy'])}</a>
        <a href="/support/?lang={lang}">{escape(n['support'])}</a>
        <a href="/terms/?lang={lang}">{escape(n['terms'])}</a>
        <a href="/data/?lang={lang}">{escape(n['data'])}</a>
        <a href="/info/?lang={lang}">{escape(n['info'])}</a>
      </nav>
    </div>
  </footer>"""


def render_page(page_key):
    ko = PAGES[page_key]["ko"]
    canonical = f"https://app.adeliedraw.com/{page_key}/"
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{LANGS[lang]["html_lang"]}" href="{canonical}?lang={lang}">'
        for lang in LANGS
    )
    panels = []
    for lang in LANGS:
        data = PAGES[page_key][lang]
        c = COMMON[lang]
        toc = "".join(
            f'<li><a href="#s-{lang}-{idx}"><span>{idx:02d}</span><span>{escape(title)}</span></a></li>'
            for idx, (title, _) in enumerate(data["sections"], 1)
        )
        sections = "".join(
            f'<section class="legal-section" id="s-{lang}-{idx}"><h2>{escape(title)}</h2>{"".join(render_item(item) for item in items)}</section>'
            for idx, (title, items) in enumerate(data["sections"], 1)
        )
        lang_links = ""
        for code, meta in LANGS.items():
            current = ' aria-current="true"' if code == lang else ""
            lang_links += (
                f'<a href="?lang={code}" data-lang-link="{code}"{current}>'
                f'{escape(meta["label"])}</a>'
            )
        panels.append(f"""
  <div data-locale="{lang}"{' hidden' if lang != 'ko' else ''}>
    {header(page_key, lang)}
    <main id="main-{lang}">
      <section class="legal-hero wrap">
        <aside class="legal-folio">
          <p class="legal-kicker">ADELIE PAGES · {escape(NAV[lang][page_key]).upper()}</p>
          <dl>
            <div><dt>APP</dt><dd>{escape(c['app'])}</dd></div>
            <div><dt>{escape(c['updated'])}</dt><dd>{UPDATED}</dd></div>
            <div><dt>{escape(c['contact'])}</dt><dd><a href="mailto:adeliedraw@gmail.com">adeliedraw@gmail.com</a></dd></div>
          </dl>
        </aside>
        <div class="legal-title">
          <h1>{escape(data['display']).replace(chr(10), '<br>')}</h1>
          <p class="legal-summary">{escape(data['summary'])}</p>
          <div class="lang-list" aria-label="Language">{lang_links}</div>
        </div>
      </section>
      <div class="legal-layout wrap">
        <aside class="legal-index"><h2>{escape(c['contents'])}</h2><ol>{toc}</ol></aside>
        <article class="legal-body">
          {sections}
          <section class="legal-section" id="contact-{lang}">
            <h2>{escape(c['contact'])}</h2>
            <dl class="legal-contact">
              <div><dt>{escape(c['operator'])}</dt><dd>{escape(c['operator'])}</dd></div>
              <div><dt>{escape(c['email'])}</dt><dd><a href="mailto:adeliedraw@gmail.com">adeliedraw@gmail.com</a></dd></div>
              <div><dt>{escape(c['phone'])}</dt><dd><a href="tel:+821063689828">+82 10-6368-9828</a></dd></div>
              <div><dt>{escape(c['address'])}</dt><dd>{escape(c['address_value'])}</dd></div>
            </dl>
          </section>
        </article>
      </div>
    </main>
    {footer(lang)}
  </div>""")
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(ko['title'])} — Adelie Pages</title>
  <meta name="description" content="{escape(ko['summary'])}">
  <meta name="theme-color" content="#f8f8f8">
  <link rel="canonical" href="{canonical}">
{alternates}
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <link rel="icon" type="image/png" href="/assets/img/brand/app-icon.png">
  <link rel="preload" href="/assets/fonts/LINESeedKR-Rg.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/legal.css">
</head>
<body>
{''.join(panels)}
  <script src="/legal.js" defer></script>
</body>
</html>
"""


def main():
    for key in PAGES:
        directory = ROOT / key
        directory.mkdir(exist_ok=True)
        (directory / "index.html").write_text(render_page(key), encoding="utf-8")


if __name__ == "__main__":
    main()
