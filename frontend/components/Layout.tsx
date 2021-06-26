import React from 'react'

import { Box, Flex, Grid, GridItem } from '@chakra-ui/react'

import { Channels } from './Channels'
import { Chat } from './Chat'
import { Topbar } from './Topbar'
import { Sidebar } from './Sidebar'

import messages from './__mocks/messages.json'
import user from './__mocks/user.json'

const Layout = () => {
	return (
		<Flex>
			<Box>
				<Sidebar />
			</Box>
			<Box flex="1">
				<Topbar />
				<Grid templateColumns="repeat(6, 1fr)" gap={1}>
					<GridItem colSpan={1} h="10">
						<Channels />
					</GridItem>
					<GridItem colSpan={4} h="10">
						<Chat messages={messages} user={user} />
					</GridItem>
					<GridItem colSpan={1} h="10">
						<Box w="40px" h="40px" bg="pink.100">
							3
						</Box>
					</GridItem>
				</Grid>
			</Box>
		</Flex>
	)
}

export default Layout
