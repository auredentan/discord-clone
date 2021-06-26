import React, { useMemo, useState, useCallback, useRef } from 'react'

import { Button, Stack } from '@chakra-ui/react'

import { ChatMessageCard } from '../ChatMessageCard'
import { ChatMessage, User } from 'types/chat'
import useWebSocket, { ReadyState } from 'react-use-websocket'

export interface ChatProps {
	messages: ChatMessage[]
	user: User
}
export const Chat = ({ messages, user }: ChatProps) => {
	const channelId = 'test'
	const [socketUrl, setSocketUrl] = useState(
		`ws://localhost:8000/channel/${channelId}/chat`
	)
	const messageHistory = useRef([])

	const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl, {
		onOpen: () => console.log('opened'),
		//Will attempt to reconnect on all close events, such as server shutting down
		shouldReconnect: (closeEvent) => true,
	})

	messageHistory.current = useMemo(
		() => messageHistory.current.concat(lastMessage),
		[lastMessage]
	)

	const handleClickChangeSocketUrl = useCallback(
		() => setSocketUrl('wss://demos.kaazing.com/echo'),
		[]
	)

	const handleClickSendMessage = useCallback(() => sendMessage('Hello'), [])

	const connectionStatus = {
		[ReadyState.CONNECTING]: 'Connecting',
		[ReadyState.OPEN]: 'Open',
		[ReadyState.CLOSING]: 'Closing',
		[ReadyState.CLOSED]: 'Closed',
		[ReadyState.UNINSTANTIATED]: 'Uninstantiated',
	}[readyState]

	console.log('messageHistory', messageHistory)
	console.log('messageHistory', messageHistory.current)

	return (
		<Stack direction={['column']} spacing="24px">
			<Button onClick={handleClickSendMessage}>dada</Button>
			{messages.map((message, index) => (
				<ChatMessageCard key={index} user={user} message={message} />
			))}
		</Stack>
	)
}
