import React from 'react'

import { Meta } from '@storybook/react'

import { Chat } from './Chat'

import messages from '../__mocks/messages.json'
import user from '../__mocks/user.json'

export default {
	component: Chat,
	title: 'Components/Chat',
} as Meta

export const Base: React.VFC = () => {
	return <Chat messages={messages} user={user} />
}
