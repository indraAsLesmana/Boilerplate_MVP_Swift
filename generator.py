def generate(inputName: str = "Test", folderPath: str = ""):
    fScreen = open(f"{folderPath}/HC{inputName}Screen.swift", "w")
    fScreen.write("import Foundation\n"
                  "import HCBaseModule\n"
                  "import HCViewModule\n\n"
                  f"public protocol HC{inputName}ScreenDelegate: HCVMVPViewDelegateBase {{\n"
                  "\n"
                  f"}}"
                  "\n"
                  f"open class HC{inputName}Screen: MVPViewController<HC{inputName}ScreenDelegate, HC{inputName}ScreenModel> {{\n"
                  "\n"
                  f"}}")
    fScreen.close()

    # Model class
    fModel = open(f"{folderPath}/HC{inputName}ScreenModel.swift", "w")
    fModel.write("import Foundation\n"
                 "import HCBaseModule\n\n"
                 f"open class HC{inputName}ScreenModel: HCMVPModel {{\n"
                 f"\tpublic var trackableName: String?\n"
                 "\trequired public init() {}\n"
                 f"}}")
    fModel.close()

    # Presenter class
    fPresenter = open(f"{folderPath}/HC{inputName}ScreenPresenter.swift", "w")
    fPresenter.write("import Foundation\n"
                     "import HCBaseModule\n"
                     "import HCViewModule\n\n"
                     f"open class HC{inputName}ScreenPresenter: MVPPresenter<HC{inputName}Screen, HC{inputName}ScreenModel> {{\n"
                     f"\tpublic required init() {{}}\n"
                     f"}}\n"
                     f"extension HC{inputName}ScreenPresenter: HC{inputName}ScreenDelegate {{\n"
                     f"\tpublic func onBackBtnPressed(_ screen: HC{inputName}Screen) {{\n"
                     f"\t\tscreen.dismiss()\n"
                     f"\t}}\n"
                     f"}}\n"
                     f"extension HCSaiHookOfferScreenPresenter {{\n"
                     "\n"
                     f"}}"
                     )
    fPresenter.close()


print("Input path folder name>>>")
folderPath = str(input().strip())
if folderPath == "":
    raise Exception("path folder must be input")

print("Input class name>>>")
className = str(input().strip())
if className == "":
    raise Exception("className must be input")

print("Input xcodeproj path>>>")
xcodeprojPath = str(input().strip())
if xcodeprojPath == "":
    raise Exception("className must be input")

generate(className, folderPath)

