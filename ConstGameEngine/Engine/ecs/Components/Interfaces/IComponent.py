from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'init') and callable(subclass.init) and hasattr(subclass, 'connect') and callable(
            subclass.connect) or NotImplemented)

    @abstractmethod
    def init(self):
        """
        Initialize all variables
        :return: None
        """

        raise NotImplementedError

    @abstractmethod
    def connect(self, entity):
        """
        'entity.set_component(self)'
        :param entity: Class
        :return: None
        """

        raise NotImplementedError
