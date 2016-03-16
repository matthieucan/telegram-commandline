#!/usr/bin/env python

import telepot
import argparse

def _get_bot(key):
    """ Returns a bot initiated with an API token. """
    bot = telepot.Bot(key)
    return bot

def send_text(args):
    bot = _get_bot(args.token)
    bot.sendMessage(args.recipient, args.message)

def send_image(args):
    bot = _get_bot(args.token)
    with open(args.path) as f:
        bot.sendPhoto(args.recipient, f)

def send_video(args):
    bot = _get_bot(args.token)
    with open(args.path) as f:
        bot.sendVideo(args.recipient, f)

def main():
    # top-level parser
    parser = argparse.ArgumentParser(description='Telebot command line.')
    subparsers = parser.add_subparsers(
        help='Command to execute. Use with --help to see its possible arguments.')
    
    # text command parser
    parser_text = subparsers.add_parser('text', help='Sends a text message.')
    parser_text.add_argument('--message',
                             help="The message to send.",
                             required=True)
    parser_text.set_defaults(func=send_text)

    # image command parser
    parser_image = subparsers.add_parser('image', help='Sends an image.')
    parser_image.add_argument('--path',
                             help="The image path.",
                             required=True)
    parser_image.set_defaults(func=send_image)

    # video command parser
    parser_video = subparsers.add_parser('video', help='Sends a video.')
    parser_video.add_argument('--path',
                             help="The video path.",
                             required=True)
    parser_video.set_defaults(func=send_video)

    # common arguments
    for p in [parser_text, parser_image, parser_video]:
        p.add_argument('--token',
                       help="Your API token.",
                       required=True)
        p.add_argument('--recipient',
                       help="Recipient ID (individual or group).",
                       required=True,
                       type=int)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
