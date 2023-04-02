# Dekoder - wersja deweloperska
# - Wykrywa błędy w odebranych segmentach.
# - Scala otrzymane segmenty w wiadomość
# - Pozbywa się narzutu z otrzymanej wiadomości.
import numpy


class Decoder:
    # -----------------------------------------------------------------------
    # Wprowadza segment bitowy do dekodera.
    #
    # Parametry:
    # segment - segment bitowy wchodzący do dekodera
    #
    # Zwraca:
    # Nic.
    # -----------------------------------------------------------------------
    def push_segment(self, segment: numpy.array):
        return

    # -----------------------------------------------------------------------
    # Wyciąga wiadomość bitową z dekodera.
    #
    # Zwraca:
    # Segment wiadomość bitową (scalone segmenty) znajduącą się w dekoderze.
    # -----------------------------------------------------------------------
    def pop_message(self) -> numpy.array:
        return numpy.array(0)