import React from 'react'

import { Meta } from '@storybook/react'

import { ChatMessageActionBar } from './ChatMessageActionBar'

export default {
	component: ChatMessageActionBar,
	title: 'Components/ChatMessageActionBar',
} as Meta

export const Base: React.VFC = () => {
	return <ChatMessageActionBar />
}
