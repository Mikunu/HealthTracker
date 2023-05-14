from windows_toasts import InteractableWindowsToaster, ToastDisplayImage, ToastImageAndText1, \
    ToastButton, ToastButtonColour, ToastActivatedEventArgs, ToastSelection, ToastInputSelectionBox, \
    ToastInputTextBox, ToastScenario
import logging


class Notifier:
    def __init__(self):
        self.path_to_resources = r'C:\\Users\nonam\PycharmProjects\aihelper\resources\drug.png'
        self.wintoaster_drugs = InteractableWindowsToaster('')


    def make_drugs_toast(self, drugs_text: str):
        newToast = ToastImageAndText1()

        newToast.AddImage(ToastDisplayImage.fromPath(self.path_to_resources))
        newToast.SetBody(drugs_text)

        newToast.SetScenario(ToastScenario.Reminder)

        toast_selections = (ToastSelection('ok', 'Хорошее'),
                            ToastSelection('medium', 'Среднее'), ToastSelection('bad', 'Плохое'))
        selection_box_input = ToastInputSelectionBox('drugs_allergy', 'Состояние:', toast_selections,
                                                     default_selection=toast_selections[0])
        newToast.AddInput(selection_box_input)
        newToast.AddInput(ToastInputTextBox('state_info_extra', 'Дополнительная информация о состоянии:'))

        okButton = ToastButton('Готово', arguments='ok', colour=ToastButtonColour.Green)
        newToast.AddAction(okButton)

        newToast.on_activated = self.activated_callback

        return newToast

    def send_drugs_notify(self, drugs_text: str):
        toast = self.make_drugs_toast(drugs_text)
        self.wintoaster_drugs.show_toast(toast)

    def activated_callback(self, activated_event_args: ToastActivatedEventArgs):
        if activated_event_args.inputs['state_info_extra'] != '':
            logging_message = f'Дополнительная информация: {activated_event_args.inputs["state_info_extra"]}'
        else:
            logging_message = ''

        if activated_event_args.inputs['drugs_allergy'] == 'ok':
            logging.info(f'Состояние: Хорошее. {logging_message}')
        if activated_event_args.inputs['drugs_allergy'] == 'medium':
            logging.warning(f'Состояние: Среднее. {logging_message}')
        if activated_event_args.inputs['drugs_allergy'] == 'bad':
            logging.critical(f'Состояние: Плохое. {logging_message}')
