def generate(inputName: str = "Test"):
    fScreen = open(f"./HC{inputName}Screen.swift", "w")
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
    fModel = open(f"./HC{inputName}ScreenModel.swift", "w")
    fModel.write("import Foundation\n"
                 "import HCBaseModule\n\n"
                 f"open class HC{inputName}ScreenModel: HCMVPModel {{\n"
                 f"\tpublic var trackableName: String?\n"
                 "\trequired public init() {}\n"
                 f"}}")
    fModel.close()

    # Presenter class
    fPresenter = open(f"./HC{inputName}ScreenPresenter.swift", "w")
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


print("Input class name")
className = str(input())
generate(className)
