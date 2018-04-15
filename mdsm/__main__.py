#!/usr/bin/env python3
import argparse
import email.utils
import mailbox
import sys
from getpass import getuser
from pathlib import Path
from socket import gethostname


class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action: argparse.Action) -> str:
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + '=' + args_string


def parse_args() -> argparse.Namespace:
    default_user = getuser() + '@' + gethostname()

    parser = argparse.ArgumentParser(
        prog='mdsm',
        formatter_class=(
            lambda prog: CustomHelpFormatter(prog, max_help_position=40)
        )
    )

    parser.add_argument(
        '-m', '--maildir', metavar='PATH', type=Path, required=True,
        help='path to the maildir where to put the e-mail in'
    )
    parser.add_argument('-s', '--subject', help='e-mail subject')
    parser.add_argument(
        '-f', '--from', dest='sender', metavar='ADDRESS',
        default=default_user,
        help='sender to send the e-mail from'
    )
    parser.add_argument(
        '-t', '--to', dest='recipient', metavar='ADDRESS',
        default=default_user,
        help='recipient to send the e-mail to'
    )
    return parser.parse_args()


def create_mail(args: argparse.Namespace) -> mailbox.mboxMessage:
    msg = mailbox.mboxMessage()
    msg['Date'] = email.utils.formatdate()
    msg['Subject'] = args.subject
    msg['From'] = args.sender
    msg['To'] = args.recipient
    msg.set_payload(sys.stdin.read())
    return msg


def send_mail(args: argparse.Namespace) -> None:
    if not (args.maildir / 'cur').exists():
        raise FileNotFoundError(
            f'"{args.maildir}" does not appear to be a valid mail directory.'
        )

    mail = create_mail(args)
    destination = mailbox.Maildir(args.maildir)
    destination.add(mail)
    destination.flush()


def main() -> None:
    try:
        args = parse_args()
        send_mail(args)
    except FileNotFoundError as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
