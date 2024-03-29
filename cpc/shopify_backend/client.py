import logging

# noinspection PyPackageRequirements
import shopify
from django.conf import settings
from pyactiveresource.connection import ResourceNotFound

logger = logging.getLogger(__name__)


class ShopifyClient:
    _instance = None

    @staticmethod
    def instance() -> "ShopifyClient":
        if ShopifyClient._instance is None:
            ShopifyClient()
        return ShopifyClient._instance

    def __init__(
        self,
        shop_url=settings.SHOPIFY_SHOP_URL,
        access_token=settings.SHOPIFY_ACCESS_TOKEN,
        api_version=settings.SHOPIFY_API_VERSION,
        _shopify=shopify,
    ):
        if ShopifyClient._instance is None:
            self._shopify = _shopify
            session = self._shopify.Session(shop_url, api_version, access_token)
            self._shopify.ShopifyResource.activate_session(session)
            ShopifyClient._instance = self
        else:
            logger.error(
                "ShopifyClient is a singleton and should not be instantiated more than once"
            )

    @property
    def active(self) -> bool:
        return self._shopify.Shop.current() is not None

    def find_product(self, **kwargs):
        try:
            if kwargs.get("id") is not None:
                return self._shopify.Product.find(kwargs.get("id"))
            return self._shopify.Product.find_first(**kwargs)
        except ResourceNotFound as e:
            logger.warning(f"Product not found: {e}")
            return None
