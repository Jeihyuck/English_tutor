{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "view-in-github"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Jeihyuck/English_tutor/blob/main/step1_basic_chat_component.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6oHLbwOtGx0P",
        "outputId": "b36117f5-b36a-4463-b5b5-ef9db389c237"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.34.0-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting altair<6,>=4.0 (from streamlit)\n",
            "  Downloading altair-5.3.0-py3-none-any.whl.metadata (9.2 kB)\n",
            "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
            "  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)\n",
            "Collecting cachetools<6,>=4.0 (from streamlit)\n",
            "  Downloading cachetools-5.3.3-py3-none-any.whl.metadata (5.3 kB)\n",
            "Collecting click<9,>=7.0 (from streamlit)\n",
            "  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: numpy<2,>=1.19.3 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=16.8 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (24.0)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (2.2.1)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (10.3.0)\n",
            "Collecting protobuf<5,>=3.20 (from streamlit)\n",
            "  Downloading protobuf-4.25.3-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)\n",
            "Collecting pyarrow>=7.0 (from streamlit)\n",
            "  Downloading pyarrow-16.1.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (2.31.0)\n",
            "Collecting rich<14,>=10.14.0 (from streamlit)\n",
            "  Downloading rich-13.7.1-py3-none-any.whl.metadata (18 kB)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (8.2.3)\n",
            "Collecting toml<2,>=0.10.1 (from streamlit)\n",
            "  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (4.10.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (3.1.43)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /home/codespace/.local/lib/python3.10/site-packages (from streamlit) (6.4)\n",
            "Collecting watchdog>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl.metadata (37 kB)\n",
            "Requirement already satisfied: jinja2 in /home/codespace/.local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /home/codespace/.local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (4.21.1)\n",
            "Collecting toolz (from altair<6,>=4.0->streamlit)\n",
            "  Downloading toolz-0.12.1-py3-none-any.whl.metadata (5.1 kB)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /home/codespace/.local/lib/python3.10/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
            "Collecting markdown-it-py>=2.2.0 (from rich<14,>=10.14.0->streamlit)\n",
            "  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/codespace/.local/lib/python3.10/site-packages (from rich<14,>=10.14.0->streamlit) (2.17.2)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /home/codespace/.local/lib/python3.10/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /home/codespace/.local/lib/python3.10/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.34.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /home/codespace/.local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
            "Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit)\n",
            "  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)\n",
            "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.10/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.34.0-py2.py3-none-any.whl (8.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.5/8.5 MB\u001b[0m \u001b[31m22.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
            "\u001b[?25hDownloading altair-5.3.0-py3-none-any.whl (857 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m857.8/857.8 kB\u001b[0m \u001b[31m10.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
            "\u001b[?25hDownloading blinker-1.8.2-py3-none-any.whl (9.5 kB)\n",
            "Downloading cachetools-5.3.3-py3-none-any.whl (9.3 kB)\n",
            "Downloading click-8.1.7-py3-none-any.whl (97 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m97.9/97.9 kB\u001b[0m \u001b[31m3.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading protobuf-4.25.3-cp37-abi3-manylinux2014_x86_64.whl (294 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m294.6/294.6 kB\u001b[0m \u001b[31m9.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyarrow-16.1.0-cp310-cp310-manylinux_2_28_x86_64.whl (40.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m40.8/40.8 MB\u001b[0m \u001b[31m15.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m26.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
            "\u001b[?25hDownloading rich-13.7.1-py3-none-any.whl (240 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m240.7/240.7 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m\n",
            "\u001b[?25hDownloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
            "Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m87.5/87.5 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading toolz-0.12.1-py3-none-any.whl (56 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m56.1/56.1 kB\u001b[0m \u001b[31m1.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
            "Installing collected packages: watchdog, toolz, toml, pyarrow, protobuf, mdurl, click, cachetools, blinker, pydeck, markdown-it-py, rich, altair, streamlit\n",
            "Successfully installed altair-5.3.0 blinker-1.8.2 cachetools-5.3.3 click-8.1.7 markdown-it-py-3.0.0 mdurl-0.1.2 protobuf-4.25.3 pyarrow-16.1.0 pydeck-0.9.1 rich-13.7.1 streamlit-1.34.0 toml-0.10.2 toolz-0.12.1 watchdog-4.0.0\n",
            "Requirement already satisfied: numpy in /home/codespace/.local/lib/python3.10/site-packages (1.26.4)\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2024-05-23 06:28:47.631 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /home/codespace/.local/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "!pip install numpy\n",
        "\n",
        "import streamlit as st\n",
        "import numpy as np\n",
        "\n",
        "with st.chat_message(\"user\"):\n",
        "    st.write(\"hello\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SCMNnJ0dHoJw"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyNEh+s9OhQq9i4innyfgPw/",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.13"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
