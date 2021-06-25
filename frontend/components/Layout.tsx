import React from 'react'

import { Box, Flex, HStack, Grid, Stack, GridItem } from '@chakra-ui/react'
import { Channels } from './Channels'
import { Chat } from './Chat'
import { Topbar } from './Topbar'
import { Sidebar } from './Sidebar'

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
						<Chat />
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
