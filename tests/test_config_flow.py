""" Test Mail and Packages config flow """
from homeassistant import config_entries, setup
from custom_components.mail_and_packages.const import DOMAIN
import os
from pytest_homeassistant_custom_component.async_mock import patch
import pytest
from custom_components.mail_and_packages.config_flow import (
    _validate_path,
    _test_login,
    _check_ffmpeg,
)


@pytest.mark.parametrize(
    "input_1,step_id_2,input_2,title,data",
    [
        (
            {
                "host": "imap.test.email",
                "port": "993",
                "username": "test@test.email",
                "password": "notarealpassword",
            },
            "config_2",
            {
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
            "imap.test.email",
            {
                "host": "imap.test.email",
                "port": 993,
                "username": "test@test.email",
                "password": "notarealpassword",
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
        ),
    ],
)
async def test_form(
    input_1, step_id_2, input_2, title, data, hass, mock_imap,
):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}
    # assert result["title"] == title_1

    with patch(
        "custom_components.mail_and_packages.config_flow._test_login", return_value=True
    ), patch(
        "custom_components.mail_and_packages.config_flow._validate_path",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.config_flow._check_ffmpeg",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.mail_and_packages.async_setup_entry", return_value=True,
    ) as mock_setup_entry:

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_1
        )
        assert result2["type"] == "form"
        assert result2["step_id"] == step_id_2

        result3 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_2
        )

    assert result3["type"] == "create_entry"
    assert result3["title"] == title
    assert result3["data"] == data

    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


@pytest.mark.parametrize(
    "input_1,step_id_2,input_2,title,data",
    [
        (
            {
                "host": "imap.test.email",
                "port": "993",
                "username": "test@test.email",
                "password": "notarealpassword",
            },
            "config_2",
            {
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
            "imap.test.email",
            {
                "host": "imap.test.email",
                "port": 993,
                "username": "test@test.email",
                "password": "notarealpassword",
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
        ),
    ],
)
async def test_form(
    input_1, step_id_2, input_2, title, data, hass, mock_imap_index_error,
):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}
    # assert result["title"] == title_1

    with patch(
        "custom_components.mail_and_packages.config_flow._test_login", return_value=True
    ), patch(
        "custom_components.mail_and_packages.config_flow._validate_path",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.config_flow._check_ffmpeg",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.mail_and_packages.async_setup_entry", return_value=True,
    ) as mock_setup_entry:

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_1
        )
        assert result2["type"] == "form"
        assert result2["step_id"] == step_id_2

        result3 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_2
        )

    assert result3["type"] == "create_entry"
    assert result3["title"] == title
    assert result3["data"] == data

    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


@pytest.mark.parametrize(
    "input_1,step_id_2,input_2,title,data",
    [
        (
            {
                "host": "imap.test.email",
                "port": "993",
                "username": "test@test.email",
                "password": "notarealpassword",
            },
            "config_2",
            {
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
            "imap.test.email",
            {
                "host": "imap.test.email",
                "port": 993,
                "username": "test@test.email",
                "password": "notarealpassword",
                "folder": '"INBOX"',
                "generate_mp4": False,
                "gif_duration": 5,
                "image_path": "/config/www/mail_and_packages/",
                "image_security": True,
                "scan_interval": 20,
                "resources": [
                    "amazon_packages",
                    "fedex_delivered",
                    "fedex_delivering",
                    "fedex_packages",
                    "mail_updated",
                    "ups_delivered",
                    "ups_delivering",
                    "ups_packages",
                    "usps_delivered",
                    "usps_delivering",
                    "usps_mail",
                    "usps_packages",
                    "zpackages_delivered",
                    "zpackages_transit",
                    "dhl_delivered",
                    "dhl_delivering",
                    "dhl_packages",
                    "amazon_delivered",
                ],
            },
        ),
    ],
)
async def test_form(
    input_1, step_id_2, input_2, title, data, hass, mock_imap_mailbox_error,
):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}
    # assert result["title"] == title_1

    with patch(
        "custom_components.mail_and_packages.config_flow._test_login", return_value=True
    ), patch(
        "custom_components.mail_and_packages.config_flow._validate_path",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.config_flow._check_ffmpeg",
        return_value=True,
    ), patch(
        "custom_components.mail_and_packages.async_setup", return_value=True
    ) as mock_setup, patch(
        "custom_components.mail_and_packages.async_setup_entry", return_value=True,
    ) as mock_setup_entry:

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_1
        )
        assert result2["type"] == "form"
        assert result2["step_id"] == step_id_2

        result3 = await hass.config_entries.flow.async_configure(
            result["flow_id"], input_2
        )

    assert result3["type"] == "create_entry"
    assert result3["title"] == title
    assert result3["data"] == data

    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


async def test_valid_path():
    result = await _validate_path(os.path.dirname(__file__))
    assert result


async def test_invalid_path():
    result = await _validate_path("/should/fail")
    assert not result


async def test_imap_login(mock_imap):
    result = await _test_login(
        "imap.test.email", 993, "fakeuser@test.email", "suchfakemuchpassword"
    )
    assert result


# async def test_detect_ffmpeg():
#     with patch("shutil.which") as mock_which:
#         mock_which.return_value = True
#         result = await _check_ffmpeg()
#         assert result

#         mock_which.return_value = False
#         result = await _check_ffmpeg()
#         assert result

