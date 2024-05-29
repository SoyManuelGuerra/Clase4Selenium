from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _esperar_elemento(self, selector, tipo_espera=None, tiempo_espera=30):
        """
        Método de utilidad para esperar a que un elemento cumpla con ciertas condiciones.
        Lanza una excepción con un mensaje personalizado si no se encuentra el elemento o si hay algún otro problema.
        
        Args:
        - selector (tuple): Selector del elemento.
        - tipo_espera (list, optional): Lista de tipos de espera ('presencia', 'visibilidad', 'clickeable'). Si es None, se consideran todos.
        - tiempo_espera (int, optional): Tiempo máximo de espera en segundos. Por defecto es 30 segundos.
        
        Returns:
        - WebElement: Elemento que cumple con las condiciones.
        """

        if tipo_espera is None:
            tipo_espera = ['presencia', 'visibilidad', 'clickeable']

        condiciones = {
            'presencia': EC.presence_of_element_located,
            'visibilidad': EC.visibility_of_element_located,
            'clickeable': EC.element_to_be_clickable
        }
        
        tipo_error = {
            TimeoutException: "no se encontró o no estuvo listo en el tiempo esperado",
            NoSuchElementException: "no se encontró",
            ElementNotInteractableException: "no es interactuable"
        }

        espera = WebDriverWait(self.controlador, tiempo_espera)
        elemento = None

        for condicion in tipo_espera:
            if condicion not in condiciones:
                raise ValueError(f"Condición no reconocida: {condicion}")
            
            try:
                if not elemento:
                    elemento = espera.until(condiciones[condicion](selector))
                else:
                    espera.until(condiciones[condicion](selector))
            except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
                mensaje = f"El elemento {selector} {tipo_error[type(e)]} (condición: {condicion})."
                raise AssertionError(mensaje) from e
        return elemento